# Generated by Django 4.2 on 2024-08-19 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_book_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='testing_word',
        ),
    ]
