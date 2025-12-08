import os
import django
from django.contrib.auth.models import User
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scope_system.settings')
django.setup()

from backend.models import UserProfile


def migrate_users():

    profiles_to_migrate = UserProfile.objects.filter(auth_user__isnull=True)

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
                print(f"Error creating user {username}: {e}")
                continue

            profile.auth_user = user
            profile.save()

            print(
                f"SUCCESS: Migrated User ID: {profile.userid} (Role: {profile.userrole}) -> Django User ID: {user.id}")

    print("--- Migration complete! ---")
    print("Now you can log in with TZ as username and 'FocalPassword2025' as password.")


if __name__ == '__main__':
    migrate_users()