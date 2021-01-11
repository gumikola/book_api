from book_api.management.commands.__base import BaseLoadDataCommand
from book_api.models import Author, Book


class Command(BaseLoadDataCommand):
    help = "Load data about books to database"

    @staticmethod
    def add_item(items):
        author_obj, _ = Author.objects.get_or_create(author=items["Autor"])
        Book.objects.get_or_create(
            author=author_obj, isbn=items["ISBN"], title=items["Tytuł"], genre=items["Gatunek"])
