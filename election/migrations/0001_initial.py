# Generated by Django 3.1.14 on 2022-07-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='候補者No.')),
                ('name', models.CharField(max_length=30, verbose_name='名前')),
                ('Political', models.CharField(max_length=30, verbose_name='政党')),
                ('description', models.TextField(blank=True, default='', verbose_name='説明')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='顔写真')),
            ],
        ),
    ]