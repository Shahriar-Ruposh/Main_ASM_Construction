# Generated by Django 3.2.14 on 2022-07-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_profile_pro_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pro_name',
            field=models.CharField(default='H', max_length=255),
        ),
    ]
