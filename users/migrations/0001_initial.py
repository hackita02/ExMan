# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(verbose_name='full name', max_length=255, blank=True, null=True)),
                ('groups', models.ManyToManyField(related_name='user_set', blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', blank=True, related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission')),
            ],
            options={
                'ordering': ['email'],
                'abstract': False,
            },
        ),
    ]
