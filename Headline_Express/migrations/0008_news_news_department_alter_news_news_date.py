# Generated by Django 5.0.2 on 2024-02-20 08:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Headline_Express', '0007_departments_remove_news_news_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_department',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Headline_Express.departments'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 21, 8, 20, 30, 288610, tzinfo=datetime.timezone.utc)),
        ),
    ]