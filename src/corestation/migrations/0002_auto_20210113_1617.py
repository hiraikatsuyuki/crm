# Generated by Django 3.1.5 on 2021-01-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corestation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='specialized_field',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='専門分野'),
        ),
    ]
