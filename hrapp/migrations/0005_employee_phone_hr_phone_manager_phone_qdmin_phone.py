# Generated by Django 4.1.3 on 2023-02-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0004_approvedleave_requestleave'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hr',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='qdmin',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
