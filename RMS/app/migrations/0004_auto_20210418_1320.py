# Generated by Django 3.0.7 on 2021-04-18 07:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_register_retype_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
