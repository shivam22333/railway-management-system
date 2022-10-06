# Generated by Django 3.0.7 on 2021-04-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_train_string'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger1', models.CharField(blank=True, max_length=50, null=True)),
                ('gender1', models.CharField(blank=True, max_length=50, null=True)),
                ('age1', models.IntegerField(blank=True, null=True)),
                ('passenger2', models.CharField(blank=True, max_length=50, null=True)),
                ('gender2', models.CharField(blank=True, max_length=50, null=True)),
                ('age2', models.IntegerField(blank=True, null=True)),
                ('passenger3', models.CharField(blank=True, max_length=50, null=True)),
                ('gender3', models.CharField(blank=True, max_length=50, null=True)),
                ('age3', models.IntegerField(blank=True, null=True)),
                ('passenger4', models.CharField(blank=True, max_length=50, null=True)),
                ('gender4', models.CharField(blank=True, max_length=50, null=True)),
                ('age4', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]