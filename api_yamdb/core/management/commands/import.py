from django.core.management.base import BaseCommand

from core.data_import import offline_import


class Command(BaseCommand):
    """Импорт ингредиентов."""

    help = 'Command to import ingredients'

    def handle(self, *args, **options):
        offline_import()
