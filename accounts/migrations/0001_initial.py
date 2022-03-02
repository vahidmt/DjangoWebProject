# Generated by Django 3.2.7 on 2021-11-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('lastname', models.CharField(max_length=50, verbose_name='lastname')),
                ('mobile_number', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]