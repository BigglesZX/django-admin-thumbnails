# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin.options import BaseModelAdmin
from django.db.models import FileField
from django.utils.safestring import mark_safe
from inspect import isclass

from .settings import (ADMIN_THUMBNAIL_DEFAULT_LABEL,
                       ADMIN_THUMBNAIL_THUMBNAIL_ALIAS,
                       ADMIN_THUMBNAIL_STYLE,
                       ADMIN_THUMBNAIL_BACKGROUND_STYLE)


try:
    from easy_thumbnails.fields import ThumbnailerImageField
except ImportError:
    ThumbnailerImageField = None


def thumbnail_factory(*args, **kwargs):
    MODE_DECORATOR = 'decorator'
    MODE_FUNCTION = 'function'

    label = ADMIN_THUMBNAIL_DEFAULT_LABEL
    background = kwargs.get('background', False)
    append = kwargs.get('append', True)

    ''' initial args validation '''
    if not args:
        raise TypeError(
            'admin_thumbnails.thumbnail: Either an subclass of BaseModelAdmin '
            'or a field name must be supplied as an argument'
        )

    ''' determine whether `thumbnail_factory` used as decorator or function '''
    if isclass(args[0]):
        mode = MODE_DECORATOR
        cls = args[0]

        ''' validate supplied class '''
        if not issubclass(cls, BaseModelAdmin):
            raise ValueError(
                'admin_thumbnails.thumbnail: Supplied class must be a '
                'subclass of django.contrib.admin.options.BaseModelAdmin'
            )

        ''' ensure field name has been supplied '''
        try:
            field_name = args[1]
        except IndexError:
            raise TypeError(
                'admin_thumbnails.thumbnail: Decorator must be passed the '
                'desired source field name as an argument'
            )

        ''' optional label argument '''
        try:
            label = args[2]
        except IndexError:
            pass
    else:
        mode = MODE_FUNCTION

        ''' ensure field name has been supplied '''
        try:
            field_name = args[0]
        except IndexError:
            raise TypeError(
                'admin_thumbnails.thumbnail: Function must be passed the '
                'desired source field name as an argument'
            )

        ''' optional label argument '''
        try:
            label = args[1]
        except IndexError:
            pass

    ''' define the thumbnail field method using the above configuration '''
    def admin_thumbnail(self, obj):
        field = obj._meta.get_field(field_name)
        field_value = getattr(obj, field_name)
        if not field_value:
            return ''

        if (isinstance(field, ThumbnailerImageField) and
                hasattr(field_value, ADMIN_THUMBNAIL_THUMBNAIL_ALIAS)):
            url = field_value[ADMIN_THUMBNAIL_THUMBNAIL_ALIAS].url
        elif isinstance(field, FileField):
            url = field_value.url
        else:
            raise TypeError(
                'admin_thumbnails.thumbnail: Field supplied must be an '
                'instance of Django’s `ImageField`, `FileField` or '
                'easy_thumbnails’ `ThumbnailerImageField` (received: {0})'
                .format(field.get_internal_name())
            )

        style = unpack_styles(ADMIN_THUMBNAIL_STYLE) + (
            unpack_styles(ADMIN_THUMBNAIL_BACKGROUND_STYLE) if background else '')  # noqa: E501
        return mark_safe(
            '<img src="{0}" style="{1}" alt="Thumbnail">'.format(url, style)
        )
    admin_thumbnail.short_description = label

    ''' if function mode, a simple return '''
    if mode == MODE_FUNCTION:
        return admin_thumbnail

    ''' otherwise decorate the supplied class '''
    new_field_name = '{0}_thumbnail'.format(field_name)
    setattr(cls, new_field_name, admin_thumbnail.__func__)
    if append:
        cls.readonly_fields = cls.readonly_fields + (new_field_name, )
    return cls


def unpack_styles(styles):
    ''' combine a dictionary of CSS property/value pairs into a string '''
    return '; '.join([': '.join(i) for i in styles.iteritems()])
