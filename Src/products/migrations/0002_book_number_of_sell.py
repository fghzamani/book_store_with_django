# Generated by Django 3.0.7 on 2021-08-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number_of_sell',
            field=models.IntegerField(default=0),
        ),
    ]