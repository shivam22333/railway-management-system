# Generated by Django 3.0.7 on 2021-04-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_detail_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='coach_train',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
