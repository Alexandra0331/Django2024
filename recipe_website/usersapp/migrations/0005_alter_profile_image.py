# Generated by Django 5.0.4 on 2024-04-29 16:20

from django.db import migrations, models
import usersapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar_default.jpg', upload_to=usersapp.models.user_directory_path, verbose_name='Аватар'),
        ),
    ]