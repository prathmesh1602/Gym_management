# Generated by Django 4.2 on 2023-05-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='pnumbner',
            field=models.IntegerField(),
        ),
    ]
