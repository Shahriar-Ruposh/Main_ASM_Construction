# Generated by Django 3.2.14 on 2022-07-30 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(),
        ),
    ]