# Generated by Django 3.0.2 on 2020-01-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='b_pic',
            field=models.ImageField(upload_to='media/image'),
        ),
    ]