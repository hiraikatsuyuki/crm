# Generated by Django 3.1.1 on 2020-11-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erad', '0015_auto_20201130_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='yakushoku',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='役職'),
        ),
    ]
