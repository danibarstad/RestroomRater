# Generated by Django 3.0.5 on 2020-06-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroom_rater', '0009_venue_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.IntegerField(max_length=5),
        ),
    ]
