# Generated by Django 2.1.4 on 2019-02-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='proof',
        ),
        migrations.AlterField(
            model_name='status',
            name='date_of_complent',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
