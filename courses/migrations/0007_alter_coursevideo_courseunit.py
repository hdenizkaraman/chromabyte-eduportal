# Generated by Django 3.2.7 on 2022-01-28 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_coursevideo_courseunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideo',
            name='courseunit',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.courseunits'),
        ),
    ]
