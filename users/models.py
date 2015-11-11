from authtools.models import AbstractEmailUser
from django.db import models


class User(AbstractEmailUser):
    full_name = models.CharField('full name', max_length=255, blank=True,
                                 null=True)

    # def get_full_name(self):
    #     return self.full_name
    #
    # def get_short_name(self):
    #     return self.preferred_name
