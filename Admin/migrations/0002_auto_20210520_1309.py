# Generated by Django 3.1.7 on 2021-05-20 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicyear',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='courseacademic',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='facultydesignation',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='facultydetails',
            options={'managed': False},
        ),
    ]
