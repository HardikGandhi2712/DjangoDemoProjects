# Generated by Django 4.2.3 on 2023-09-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'dept',
            },
        ),
    ]