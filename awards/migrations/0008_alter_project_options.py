# Generated by Django 4.0.3 on 2022-04-09 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0007_rename_content_rate_rate_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_posted']},
        ),
    ]
