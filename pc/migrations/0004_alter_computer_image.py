# Generated by Django 5.0 on 2023-12-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc', '0003_computer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/<built-in function id>-135', verbose_name='Photo'),
        ),
    ]
