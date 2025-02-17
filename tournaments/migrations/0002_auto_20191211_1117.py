# Generated by Django 2.2.5 on 2019-12-11 05:47

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentjoin',
            name='email',
            field=models.EmailField(default='asd@asd.com', max_length=150),
        ),
        migrations.AddField(
            model_name='tournamentjoin',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 12, 11)),
        ),
        migrations.AddField(
            model_name='tournamentjoin',
            name='location',
            field=models.CharField(default='chennai', max_length=150),
        ),
        migrations.AddField(
            model_name='tournamentjoin',
            name='name',
            field=models.CharField(default='manoj', max_length=150),
        ),
        migrations.AddField(
            model_name='tournamentjoin',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 12, 11)),
        ),
        migrations.AddField(
            model_name='tournamentjoin',
            name='tournament_name',
            field=models.CharField(default='t1', max_length=150),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentjoin',
            unique_together={('user', 'tournament')},
        ),
    ]
