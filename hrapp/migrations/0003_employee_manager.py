# Generated by Django 4.1.3 on 2023-02-02 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0002_rename_admin_qdmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrapp.manager'),
        ),
    ]
