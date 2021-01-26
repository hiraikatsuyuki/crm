# Generated by Django 3.1.1 on 2020-11-29 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erad', '0011_auto_20201028_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'e-Rad応募データ', 'verbose_name_plural': 'e-Rad応募データ'},
        ),
        migrations.AlterModelOptions(
            name='researcher',
            options={'verbose_name': 'e-Rad研究者データ', 'verbose_name_plural': 'e-Rad研究者データ'},
        ),
        migrations.AddField(
            model_name='researcher',
            name='eijishimei',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='英字氏名'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='kanashimei',
            field=models.CharField(default=1, max_length=100, verbose_name='フリガナ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='kanjishimei',
            field=models.CharField(default=1, max_length=50, verbose_name='研究者氏名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='tsuushoumei',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='通称名'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='tsuushoumei_kana',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='通称名フリガナ'),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='furigana_mei',
            field=models.CharField(default=1, max_length=50, verbose_name='フリガナ-名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='researcher',
            name='furigana_sei',
            field=models.CharField(default=1, max_length=50, verbose_name='フリガナ-姓'),
            preserve_default=False,
        ),
    ]
