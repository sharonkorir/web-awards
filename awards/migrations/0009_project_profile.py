# Generated by Django 4.0.3 on 2022-04-09 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0008_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.profile'),
        ),
    ]
