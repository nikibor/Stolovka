# Generated by Django 2.2.7 on 2019-11-19 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=10, verbose_name='Широта')),
                ('longitude', models.CharField(blank=True, max_length=10, verbose_name='Долгота')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Название')),
                ('rating', models.FloatField(blank=True, default=0, null=True, verbose_name='Рейтинг')),
                ('address', models.CharField(blank=True, max_length=300, verbose_name='Адрес')),
                ('open_hours', models.CharField(blank=True, max_length=20, null=True, verbose_name='Часы работы')),
                ('average_check', models.FloatField(blank=True, null=True, verbose_name='Средний чек')),
                ('views', models.IntegerField(blank=True, default=0, verbose_name='Количество просмотров')),
                ('feature', models.IntegerField(blank=True, choices=[(1, 'Оплата по карте'), (2, 'Алкоголь'), (3, 'Туалет'), (4, 'Гигиена на кухне'), (5, 'Вегетарианская кухня')], null=True, verbose_name='Особенность')),
            ],
            options={
                'verbose_name': 'Заведение',
                'verbose_name_plural': 'Заведения',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(blank=True, max_length=3000, verbose_name='Рецензия')),
                ('date', models.DateTimeField(blank=True, verbose_name='Дата публкации')),
                ('mark', models.IntegerField(blank=True, verbose_name='Оценка')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(blank=True, verbose_name='Пользовательская оценка')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.Place', verbose_name='Заведение')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
    ]