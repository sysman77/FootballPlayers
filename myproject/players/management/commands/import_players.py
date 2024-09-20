# players/management/commands/import_players.py
import csv
from django.core.management.base import BaseCommand
from players.models import Player  # Ujisti se, že tento import je správný

class Command(BaseCommand):
    help = 'Import players from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    id_player=row['id_player'],
                    last_name=row['last_name'],
                    first_name=row['first_name'],
                    birth_year=row['birth_year'],
                    club=row['club']
                )
                player.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported players'))
