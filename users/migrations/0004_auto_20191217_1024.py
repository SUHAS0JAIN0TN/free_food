# Generated by Django 2.2.3 on 2019-12-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
