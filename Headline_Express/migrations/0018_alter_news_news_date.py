# Generated by Django 5.0.2 on 2024-02-23 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Headline_Express', '0017_alter_news_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 24, 5, 31, 11, 310177, tzinfo=datetime.timezone.utc)),
        ),
    ]
