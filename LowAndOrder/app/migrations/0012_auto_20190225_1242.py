# Generated by Django 2.1.4 on 2019-02-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190225_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complent',
            name='station_id',
            field=models.IntegerField(),
        ),
    ]