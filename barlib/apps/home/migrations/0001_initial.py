# Generated by Django 3.2 on 2024-11-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('categoria', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
            ],
        ),
    ]