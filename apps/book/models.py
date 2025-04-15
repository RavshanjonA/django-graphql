from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, ManyToManyField, ImageField


class BookCategory(Model):
    name = CharField(max_length=255)

    class Meta:
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"

    def __str__(self):
        return self.name


class BookGenre(Model):
    name = CharField(max_length=128)

    class Meta:
        verbose_name = "Book Genre"
        verbose_name_plural = "Book Genres"

    def __str__(self):
        return self.name


class Book(Model):
    title = CharField(max_length=255)
    summary = TextField()
    cover = ImageField(upload_to="images", null=True)
    category = ForeignKey("book.BookCategory", CASCADE)
    genres = ManyToManyField("book.BookGenre")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
