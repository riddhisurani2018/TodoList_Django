# Generated by Django 2.2.5 on 2020-09-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
