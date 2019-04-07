from django.conf import settings


''' Sets the default label used for the field and column created for each
    thumbnail
'''
ADMIN_THUMBNAIL_DEFAULT_LABEL = \
    getattr(settings, 'ADMIN_THUMBNAIL_DEFAULT_LABEL', 'Preview')

''' If `easy_thumbnails` is available, model fields using
    `ThumbnailerImageField` will be displayed using this thumbnail alias (which
    must be specified within `THUMBNAIL_ALIASES` in site settings)
'''
ADMIN_THUMBNAIL_THUMBNAIL_ALIAS = \
    getattr(settings, 'ADMIN_THUMBNAIL_THUMBNAIL_ALIAS', 'admin_thumbnail')

''' The following CSS styles will be applied to thumbnails when displayed in
    the admin
'''
ADMIN_THUMBNAIL_STYLE = \
    getattr(settings, 'ADMIN_THUMBNAIL_STYLE', {
        'display': 'block',
        'width': '100px',
        'height': 'auto',
    })

''' If the `background` option is used, the following additional CSS styles
    will be applied
'''
ADMIN_THUMBNAIL_BACKGROUND_STYLE = \
    getattr(settings, 'ADMIN_THUMBNAIL_BACKGROUND_STYLE', {
        'background': '#000',
    })
