# Generated by Django 4.0.3 on 2022-04-10 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0010_alter_profile_bio_alter_profile_profile_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_photo',
        ),
    ]
