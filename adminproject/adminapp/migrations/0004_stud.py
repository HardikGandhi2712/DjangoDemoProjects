# Generated by Django 4.2.3 on 2023-09-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_item_itemorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('rno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=20)),
                ('science', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('eng', models.IntegerField()),
            ],
            options={
                'db_table': 'stud',
            },
        ),
    ]
