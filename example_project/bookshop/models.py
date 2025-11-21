from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Book(models.Model):
    title = models.CharField("Title", max_length=200)

    author = models.CharField("Author", max_length=200)

    cover = models.ImageField("Cover image", blank=True)

    cover_thumb = ThumbnailerImageField("Cover image (ThumbnailField)", blank=True)

    pages = models.IntegerField("Pages", null=True, blank=True)

    isbn_code = models.CharField("ISBN code", max_length=20, blank=True)

    @property
    def cover_property(self):
        """simple example use of model property"""
        return self.cover

    @property
    def cover_thumb_property(self):
        """simple example use of model property returning `ThumbnailerImageField`"""
        return self.cover_thumb

    def __str__(self):
        return self.title
