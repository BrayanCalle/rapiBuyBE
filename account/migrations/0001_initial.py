# Generated by Django 3.2 on 2021-07-20 03:15

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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('acronym', models.CharField(max_length=100, verbose_name='Sigla')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Número de teléfono')),
                ('street_address', models.CharField(max_length=255, verbose_name='Dirección')),
                ('email', models.EmailField(max_length=255, verbose_name='Correo electrónico')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='account.account')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
