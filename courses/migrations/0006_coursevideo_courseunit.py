# Generated by Django 3.2.7 on 2022-01-28 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_courseunits_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursevideo',
            name='courseunit',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.courseunits', null=True),
        ),
    ]
