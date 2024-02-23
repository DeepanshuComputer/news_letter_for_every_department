# Generated by Django 5.0.2 on 2024-02-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Headline_Express', '0003_rename_subs_email_subs_info_email_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_cat', models.CharField(max_length=60, unique=True)),
                ('news_img', models.ImageField(upload_to='images/')),
                ('news_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='subs_info',
            old_name='Email_Id',
            new_name='Email',
        ),
    ]