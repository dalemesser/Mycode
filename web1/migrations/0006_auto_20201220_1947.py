# Generated by Django 3.1.4 on 2020-12-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0005_auto_20201220_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discounted',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('dilivered', 'dilivered'), ('out of dilivery', 'out of dilivery'), ('pending', 'pending')], max_length=200, null=True),
        ),
    ]