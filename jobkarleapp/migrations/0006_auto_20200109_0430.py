# Generated by Django 2.2.2 on 2020-01-09 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobkarleapp', '0005_auto_20200109_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fresherqualification',
            name='Course',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobkarleapp.Qualification_Course'),
        ),
        migrations.AlterField(
            model_name='fresherqualification',
            name='Highest_Qualification',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobkarleapp.Qualification'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
