# Generated by Django 4.2.5 on 2023-12-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc', '0007_alter_computer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='computer',
            name='configuration',
            field=models.TimeField(max_length=700),
        ),
    ]
