# Generated by Django 3.1.7 on 2021-04-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inpro_home', '0002_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtype',
            name='description',
            field=models.TextField(default='item description'),
            preserve_default=False,
        ),
    ]
