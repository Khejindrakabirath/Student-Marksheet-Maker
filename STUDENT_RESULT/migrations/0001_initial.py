# Generated by Django 4.1.3 on 2022-11-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuName', models.CharField(max_length=20)),
                ('engMark', models.IntegerField()),
                ('mathMark', models.IntegerField()),
                ('sciMark', models.IntegerField()),
                ('socMark', models.IntegerField()),
                ('nepMark', models.IntegerField()),
                ('heaMark', models.IntegerField()),
            ],
        ),
    ]
