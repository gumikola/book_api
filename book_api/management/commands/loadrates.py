from book_api.management.commands.__base import BaseLoadDataCommand
from book_api.models import Book, Opinion
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseLoadDataCommand):
    help = "Load data about rates for books to database"

    @staticmethod
    def add_item(items):
        try:
            book_obj = Book.objects.get(isbn=items["ISBN"])
            Opinion.objects.get_or_create(
                isbn=book_obj, rate=items["Ocena"], describe=items["Opis"])
        except ObjectDoesNotExist:
            print(f'Book of ISBN:{items["ISBN"]} not exist. Please add book before add opinion.')
