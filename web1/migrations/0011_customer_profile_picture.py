# Generated by Django 3.1.4 on 2021-01-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0010_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
