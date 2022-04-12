import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            id = list(phone.values())[0]
            name = list(phone.values())[1]
            image = list(phone.values())[2]
            price = list(phone.values())[3]
            release_date = list(phone.values())[4]
            lte_exists = list(phone.values())[5]
            slug = slugify(name)

            phone = Phone(id=id, name=name, image=image, price=price, release_date=release_date,
                          lte_exists=lte_exists, slug=slug)
            phone.save()