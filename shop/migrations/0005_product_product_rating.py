# Generated by Django 2.2.7 on 2019-12-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20191207_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_rating',
            field=models.FloatField(default=0.0, max_length=5.0),
        ),
    ]