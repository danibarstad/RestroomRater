# Generated by Django 3.0.5 on 2020-06-17 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroom_rater', '0008_auto_20200605_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='category',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
