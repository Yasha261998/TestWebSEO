# Generated by Django 3.2.7 on 2021-09-22 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, verbose_name='Имя продавца')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, verbose_name='Название товара')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, verbose_name='Имя')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
                ('last_time', models.DateTimeField(auto_now_add=True, verbose_name='Время последнего входа')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price_sale', models.FloatField(verbose_name='Цена')),
                ('number', models.IntegerField(verbose_name='Количество')),
                ('dt_sale', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время покупки')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.items')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.employees')),
            ],
        ),
    ]
