# Generated by Django 4.1.5 on 2023-02-18 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='home.color'),
        ),
    ]
