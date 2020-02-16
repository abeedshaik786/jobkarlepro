# Generated by Django 2.2.2 on 2020-02-10 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobkarleapp', '0006_auto_20200109_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fresherqualification',
            name='Course',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobkarleapp.Qualification_Course'),
        ),
        migrations.AlterField(
            model_name='fresherqualification',
            name='Resume',
            field=models.FileField(upload_to='Resume'),
        ),
    ]
