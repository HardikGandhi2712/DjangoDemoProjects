# Generated by Django 4.2.3 on 2023-09-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
    ]
