# Generated by Django 2.2.7 on 2019-12-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='prize',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
