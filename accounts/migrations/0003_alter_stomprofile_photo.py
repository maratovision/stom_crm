# Generated by Django 3.2 on 2021-04-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210409_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stomprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
