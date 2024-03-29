# Generated by Django 3.2.7 on 2022-01-28 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_coursevideo_courseunit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursevideo',
            name='courseunit',
        ),
        migrations.AddField(
            model_name='courseunits',
            name='videoindex_end',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='courseunits',
            name='videoindex_start',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coursevideo',
            name='courselist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='video_plist', to='courses.courselist'),
        ),
    ]
