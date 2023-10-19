from django.core.management.base import BaseCommand
from news.models import Post


class Command(BaseCommand):
    help = 'Удаление новостей'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write(
            'Все новости будут удалены yes/no')
        answer = input()

        if answer == 'yes':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped products!'))
            return

        self.stdout.write(
            self.style.ERROR('Access denied'))
