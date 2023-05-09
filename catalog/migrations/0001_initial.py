# Generated by Django 4.1 on 2023-05-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordid', models.CharField(help_text='ID of the word ', max_length=20)),
                ('word', models.CharField(help_text='word itself', max_length=40)),
                ('definition', models.CharField(help_text='Meanings of the word', max_length=100)),
            ],
            options={
                'ordering': ['wordid'],
            },
        ),
    ]
