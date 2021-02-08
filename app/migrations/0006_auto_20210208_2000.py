# Generated by Django 3.1.2 on 2021-02-08 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201208_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.team'),
        ),
        migrations.AlterField(
            model_name='nationalmember',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.team'),
        ),
    ]