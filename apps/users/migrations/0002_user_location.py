# Generated by Django 5.0.2 on 2024-04-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]