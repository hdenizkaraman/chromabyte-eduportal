# Generated by Django 3.2.7 on 2022-01-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_arma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arma',
            name='armaimage',
            field=models.ImageField(default='armaimage/sirdenq.png', upload_to='armaimage/'),
        ),
    ]
