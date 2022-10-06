# Generated by Django 3.0.7 on 2021-04-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_detail_coach_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='seat1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='seat2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='seat3',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='seat4',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='train',
            name='tfirst_ac',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='train',
            name='tsc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='train',
            name='tsecond_ac',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='train',
            name='tthird_ac',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='age1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='age2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='age3',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='age4',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='pnr',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]