# Generated by Django 5.0.4 on 2024-04-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_recipe_cooking_time_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.DurationField(verbose_name='Время приготовления (мин:сек)'),
        ),
    ]