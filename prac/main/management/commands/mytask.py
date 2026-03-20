from django.core.management.base import BaseCommand
import time

class Command(BaseCommand):
    # help = 'Run my  Schedule task'

    def handle(self, *args, **kwargs):
        for i in range(5):   # run 5 times
            print(f"Task running demo {i+1}")
            time.sleep(2)