# Generated by Django 5.0.6 on 2024-08-02 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='film_director', to='movies.actor', verbose_name='Режиссер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Слоган'),
        ),
    ]
