# Generated by Django 3.1.7 on 2021-11-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211129_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationalmember',
            name='selected_year',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]