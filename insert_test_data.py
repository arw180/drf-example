import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '.')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings'

from django.contrib.auth.models import User

import myapp.models as models

import django
django.setup()

def run():
    # create some users
    user_data = [
        {
            'username': 'bob',
            'email': 'bob@google.com',
            'password': 'password'
        },
        {
            'username': 'alice',
            'email': 'alice@google.com',
            'password': 'password'
        },
        {
            'username': 'jill',
            'email': 'jill@google.com',
            'password': 'password'
        }
    ]
    for i in user_data:
        user = User.objects.create_user(
            username=i['username'], email=i['email'], password=i['password'])
        user.save()

    # create some profiles
    user = User.objects.get(username='bob')
    bob = models.Profile(display_name='Bob Smith', user=user)
    bob.save()

    user = User.objects.get(username='alice')
    alice = models.Profile(display_name='Alice Jones', user=user)
    alice.save()

    user = User.objects.get(username='jill')
    jill = models.Profile(display_name='Jill Brown', user=user)
    jill.save()

    # create some categories
    business = models.Category(name="Business",
        description="Things for making money")
    business.save()

    fun = models.Category(name="Fun",
        description="Things for playing")
    fun.save()

    productivity = models.Category(name="Productivity",
        description="Things for being productive")
    productivity.save()

    # create some listings
    money_printer = models.Listing(title='Money Printer',
        category=business)
    money_printer.save()
    money_printer.owners.add(jill)
    money_printer.owners.add(bob)

if __name__ == "__main__":
    run()