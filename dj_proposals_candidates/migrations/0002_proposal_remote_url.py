# Generated by Django 3.1.6 on 2021-02-14 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_proposals_candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='remote_url',
            field=models.URLField(blank=True),
        ),
    ]
