# Generated by Django 4.0.4 on 2022-04-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specs',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
