# Generated by Django 3.2.10 on 2021-12-27 17:18

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=80, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('identification_number', models.CharField(max_length=10, verbose_name='Número de identificación')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Número de teléfono')),
                ('street', models.CharField(max_length=50, verbose_name='Calle Principal')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('country', models.CharField(max_length=50, verbose_name='País')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Código Postal')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
