# Generated by Django 5.0.2 on 2024-02-22 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Headline_Express', '0016_alter_news_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 23, 10, 34, 17, 930316, tzinfo=datetime.timezone.utc)),
        ),
    ]