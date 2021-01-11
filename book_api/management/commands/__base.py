import csv

from django.core.management.base import BaseCommand, CommandError


class BaseLoadDataCommand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "path", type=str, help="Path to file which contain data to import")

    def handle(self, *args, **options):
        path_to_file = options["path"]

        try:
            with open(path_to_file, mode="r") as file:
                for row in csv.DictReader(file, delimiter=";"):
                    self.add_item(row)
        except FileNotFoundError:
            raise CommandError("Bad path to file")

        self.stdout.write(self.style.SUCCESS("Completed import!"))

    @staticmethod
    def add_item(items):
        pass
