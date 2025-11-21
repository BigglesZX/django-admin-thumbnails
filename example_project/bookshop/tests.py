from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookAdminViewTests(TestCase):
    def setUp(self):
        User.objects.create_superuser(username="test", password="test")
        self.client.login(
            username="test",
            password="test",
        )

        Book.objects.create(
            title="Lorem Ipsum Dolor",
            author="A Smith",
            cover="cover1.jpg",
            cover_thumb="cover1.jpg",
            pages=123,
            isbn_code="1234567890",
        )

    def test_book_changelist_view(self):
        response = self.client.get(reverse("admin:bookshop_book_changelist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            """
            <td class="field-cover_thumbnail">
                <img src="/media/cover1.jpg" style="display: block; width: 100px; height: auto" alt="Thumbnail">
            </td>
            """,
            html=True,
        )
        self.assertContains(
            response,
            """
            <td class="field-cover_thumb_thumbnail">
                <img src="/media/thumbnails/cover1.jpg.200x200_q85_background-%23fff.jpg" style="display: block; width: 100px; height: auto" alt="Thumbnail">
            </td>
            """,
            html=True,
        )

    def test_book_change_view(self):
        response = self.client.get(reverse("admin:bookshop_book_change", args=["1"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            """
            <div class="form-row field-cover_thumbnail">
                <div>
                    <div class="flex-container">
                        <label>Cover image:</label>
                        <div class="readonly">
                            <img src="/media/cover1.jpg" style="display: block; width: 100px; height: auto" alt="Thumbnail">
                        </div>
                    </div>
                </div>
            </div>
            """,
            html=True,
        )
        self.assertContains(
            response,
            """
            <div class="form-row field-cover_thumb_thumbnail">
                <div>
                    <div class="flex-container">
                        <label>Cover image (ThumbnailField):</label>
                        <div class="readonly"><img src="/media/thumbnails/cover1.jpg.200x200_q85_background-%23fff.jpg" style="display: block; width: 100px; height: auto" alt="Thumbnail"></div>
                    </div>
                </div>
            </div>""",
            html=True,
        )
