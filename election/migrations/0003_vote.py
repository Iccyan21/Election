# Generated by Django 3.1.14 on 2022-07-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_candidate_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
            ],
        ),
    ]
