# Generated by Django 3.0.7 on 2021-04-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210421_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
