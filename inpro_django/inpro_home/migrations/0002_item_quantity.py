# Generated by Django 3.1.7 on 2021-04-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inpro_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]