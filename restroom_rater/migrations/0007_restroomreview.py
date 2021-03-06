# Generated by Django 3.0.5 on 2020-06-05 03:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restroom_rater', '0006_auto_20200604_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestroomReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField()),
                ('number', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(limit_value=0))),
                ('rest_type', models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('U', 'Unisex'), ('F', 'Family')], default='M', max_length=1)),
                ('baby', models.BooleanField()),
                ('needle', models.BooleanField()),
                ('handicap', models.BooleanField()),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1)),
                ('title', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=1000)),
                ('posted_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restroom_rater.Venue')),
            ],
        ),
    ]
