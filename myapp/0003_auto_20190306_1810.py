# Generated by Django 2.0.1 on 2019-03-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190306_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='usersave',
            name='location',
        ),
        migrations.RemoveField(
            model_name='usersave',
            name='profile_photo',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_photo',
            field=models.ImageField(max_length=100000000, upload_to=''),
        ),
    ]
