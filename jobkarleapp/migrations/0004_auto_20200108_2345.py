# Generated by Django 2.2.2 on 2020-01-09 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobkarleapp', '0003_auto_20200108_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fresherdata',
            name='fresher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobkarleapp.Fresher'),
        ),
    ]
