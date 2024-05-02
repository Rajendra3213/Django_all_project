import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()
from first_app.models import User
from faker import Faker
fakegen = Faker()
def populate(N=5):
    for i in range(N):
        #fake data
        fake_username = fakegen.user_name()
        fake_email = fakegen.email()
        # Check for unique URL within the chosen topic
        while User.objects.filter(username= fake_username).exists():
            fake_username = fakegen.username()  # Generate a new URL if collision
        # Create the new page webpage entry with error handling
        try:
            User.objects.get_or_create(username=fake_username,email=fake_email)[0]
        except Exception as e:
            print(f"Error creating record: {e}")

if __name__ == '__main__':
    print("Populating")
    populate(20)
    print("population complete")