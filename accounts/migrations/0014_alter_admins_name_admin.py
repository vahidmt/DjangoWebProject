# Generated by Django 3.2.7 on 2021-12-12 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0013_alter_admins_name_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='name_admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
