# Generated by Django 3.0.8 on 2020-08-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroom_rater', '0014_auto_20200716_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restroomreview',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='restroomreview',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]