from django.db.models import Model, CharField, TextField, FileField, ForeignKey, CASCADE, ManyToManyField

from config.storage_backends import PrivateMediaStorage


class BookCategory(Model):
    # icon =
    name = CharField(max_length=255)

    class Meta:
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"


class BookGenre(Model):
    name = CharField(max_length=128)

    class Meta:
        verbose_name = "Book Genre"
        verbose_name_plural = "Book Genres"


class Book(Model):
    title = CharField(max_length=255)
    summary = TextField()
    file = FileField(upload_to="books")
    category = ForeignKey("book.BookCategory", CASCADE)
    genres = ManyToManyField("book.BookGenre")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
