# Generated by Django 5.0.4 on 2024-04-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_recipe_cooking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.DurationField(verbose_name='Время приготовления (чч:мм:сс)'),
        ),
    ]