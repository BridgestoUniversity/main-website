# Generated by Django 3.1 on 2020-09-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200930_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='linkType',
            field=models.CharField(default='A', max_length=20),
        ),
    ]
