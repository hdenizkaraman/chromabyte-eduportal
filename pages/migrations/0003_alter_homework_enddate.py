# Generated by Django 3.2.7 on 2022-01-30 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='enddate',
            field=models.DateTimeField(verbose_name='Ödev Bitiş Tarihi'),
        ),
    ]