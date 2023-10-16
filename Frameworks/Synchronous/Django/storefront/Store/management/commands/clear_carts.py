from django.core.management.base import BaseCommand, CommandError, CommandParser
from Store.models import Cart

class Command(BaseCommand):
    help = "Deletes Carts that are over a certain age"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING(f"Deleting {Cart.old_carts.count()} Carts"))
        for cart in Cart.old_carts.all():
            cart.delete()
        