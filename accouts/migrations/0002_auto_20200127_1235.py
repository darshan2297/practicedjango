# Generated by Django 3.0.2 on 2020-01-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
