# Generated by Django 3.1.4 on 2021-02-28 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('printers', '0002_auto_20210227_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Месторасположение'),
        ),
    ]
