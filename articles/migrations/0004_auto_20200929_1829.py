# Generated by Django 3.1 on 2020-09-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200929_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(default='Date has not been set'),
        ),
    ]
