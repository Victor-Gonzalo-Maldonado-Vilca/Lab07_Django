# Generated by Django 5.0.6 on 2024-06-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=100)),
                ('descripcionCiudad', models.TextField()),
                ('imagenCiudad', models.ImageField(upload_to='images/')),
                ('precioTour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ofertaTour', models.BooleanField(default=False)),
            ],
        ),
    ]