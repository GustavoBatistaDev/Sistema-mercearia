# Generated by Django 4.2.7 on 2023-11-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=1, upload_to='photo-products'),
            preserve_default=False,
        ),
    ]
