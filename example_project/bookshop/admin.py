import admin_thumbnails

from django.contrib import admin

from .models import Book


@admin.register(Book)
@admin_thumbnails.thumbnail("cover", "Cover image")
@admin_thumbnails.thumbnail("cover_thumb", "Cover image (ThumbnailField)")
@admin_thumbnails.thumbnail("cover_property", "Cover image (property)")
@admin_thumbnails.thumbnail(
    "cover_thumb_property", "Cover image (ThumbnailField, property)"
)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "pages",
        "isbn_code",
        "cover_thumbnail",
        "cover_thumb_thumbnail",
    ]
