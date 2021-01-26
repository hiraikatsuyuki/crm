# Generated by Django 3.1.1 on 2020-10-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erad', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researcher',
            old_name='department',
            new_name='bukyokumei',
        ),
        migrations.RenameField(
            model_name='researcher',
            old_name='date_of_birth',
            new_name='seinengappi',
        ),
        migrations.RenameField(
            model_name='researcher',
            old_name='title',
            new_name='shokumei',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='kanashimei_mei',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='kanashimei_sei',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='kanjishimei_mei',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='kanjishimei_sei',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='sex',
        ),
        migrations.AddField(
            model_name='researcher',
            name='furigana_mei',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='フリガナ-名'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='furigana_sei',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='フリガナ-姓'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='gakui',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='学位'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='gakuishutokunengappi',
            field=models.DateField(blank=True, null=True, verbose_name='学位取得年月日'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='kakenhiouboshikaku',
            field=models.CharField(default=1, max_length=1, verbose_name='科研費応募資格'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='kenkyuushashimei_mei',
            field=models.CharField(default=1, max_length=50, verbose_name='研究者氏名-名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='kenkyuushashimei_sei',
            field=models.CharField(default=1, max_length=50, verbose_name='研究者氏名-姓'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='mailaddress1',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス1'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='mailaddress2',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス2'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='seibetsu',
            field=models.CharField(choices=[('0', ''), ('1', '男性'), ('2', '女性'), ('9', 'その他')], default=1, max_length=1, verbose_name='性別'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='shutarukenkyuukikan',
            field=models.CharField(default=1, max_length=1, verbose_name='主たる研究機関'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='tsuushoumei_mei',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='通称名-名'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='tsuushoumei_sei',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='通称名-姓'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='tsuushoumeifurigana_mei',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='通称名フリガナ-名'),
        ),
        migrations.AddField(
            model_name='researcher',
            name='tsuushoumeifurigana_sei',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='通称名フリガナ-姓'),
        ),
    ]
