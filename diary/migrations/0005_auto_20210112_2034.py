# Generated by Django 3.1.4 on 2021-01-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20210109_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='afternoon',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='items',
            name='morning',
        ),
        migrations.RemoveField(
            model_name='items',
            name='nigth',
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(blank=True, choices=[('Studies', 'Studies'), ('My Projects', 'My Projects'), ('Entertainment', 'Entertainment'), ('Political_News', 'Political_News'), ('Bussiness_Decions', 'Bussiness_Decions')], max_length=400),
        ),
        migrations.AddField(
            model_name='items',
            name='session',
            field=models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('night', 'night')], max_length=120),
        ),
        migrations.AlterField(
            model_name='items',
            name='feedback',
            field=models.CharField(blank=True, choices=[('good', 'good'), ('bad', 'bad')], max_length=120),
        ),
    ]
