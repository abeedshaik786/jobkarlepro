# Generated by Django 2.2.2 on 2020-02-14 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobkarleapp', '0010_auto_20200213_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fresherdata',
            name='fresher',
        ),
        migrations.RemoveField(
            model_name='fresherqualification',
            name='fresher',
        ),
    ]
