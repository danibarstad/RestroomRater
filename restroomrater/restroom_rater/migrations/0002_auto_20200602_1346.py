# Generated by Django 3.0.5 on 2020-06-02 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restroom_rater', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Establishment',
            new_name='Venue',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='establishment',
            new_name='venue',
        ),
    ]