# Generated by Django 3.1 on 2020-11-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obywatele', '0009_auto_20201125_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzytkownik',
            name='location',
        ),
        migrations.AddField(
            model_name='uzytkownik',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]