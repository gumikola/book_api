from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.author


class Book(models.Model):

    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.author} - {self.title}"


class Opinion(models.Model):
    scale_of_rate = [(x, str(x))for x in range(1, 6)]

    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.IntegerField(
        choices=scale_of_rate, default=max(scale_of_rate))
    describe = models.TextField()

    def __str__(self):
        return f"{self.isbn.author} - {self.isbn.title} Rate: {self.rate}"
