import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scope_system.settings')
import django

django.setup()

from django.db import transaction
from django.contrib.auth.models import User
from backend.models import UserProfile


def migrate_users():

    profiles_to_migrate = UserProfile.objects.filter(user__isnull=True)

    print(f"--- Found {profiles_to_migrate.count()} profiles to migrate... ---")

    with transaction.atomic():
        for profile in profiles_to_migrate:
            username = profile.tz

            try:
                user = User.objects.create_user(
                    username=username,
                    email=f'{username}@focal.org.il',
                    password='FocalPassword2025'
                )

            except Exception as e:
                if 'already exists' in str(e) or 'duplicate key' in str(e):
                    print(f"SKIP: User with username {username} already exists.")
                    continue

                print(f"Error creating user {username}: {e}")
                continue


            profile.user = user
            profile.save()

            print(
                f"SUCCESS: Migrated User ID: {profile.userid} (Role: {profile.userrole}) -> Django User ID: {user.id}")

    print("--- Migration complete! ---")
    print("Now you can log in with TZ as username and 'FocalPassword2025' as password.")


if __name__ == '__main__':
    migrate_users()