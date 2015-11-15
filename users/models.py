from authtools.models import AbstractEmailUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    @classmethod
    def normalize_email(cls, email):
        return email.strip().lower()


class User(AbstractEmailUser):
    full_name = models.CharField('full name', max_length=255, blank=True,
                                 null=True)

    objects = CustomUserManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.clean()  # force call even if not called by form/view
        super().save(force_insert, force_update, using, update_fields)

    def clean(self):
        self.email = self.email.strip().lower()  # normalize email field

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name
