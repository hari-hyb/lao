# Generated by Django 2.1.4 on 2019-02-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_detective'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('citizen_id', models.AutoField(primary_key=True, serialize=False)),
                ('citizen_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email_id', models.EmailField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=10)),
                ('mobile_no', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
