# Generated by Django 3.2.7 on 2021-12-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_admins_name_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='name_admin',
            field=models.CharField(max_length=200),
        ),
    ]
