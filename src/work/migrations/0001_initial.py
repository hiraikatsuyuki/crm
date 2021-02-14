# Generated by Django 3.1.5 on 2021-02-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255, verbose_name='キーワード')),
            ],
            options={
                'verbose_name': 'キーワード',
                'verbose_name_plural': 'キーワード',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eradcode', models.CharField(max_length=8, verbose_name='研究者番号')),
                ('role', models.CharField(choices=[('1', '代表'), ('2', '分担'), ('3', '筆頭著者'), ('4', '責任著者')], max_length=1, verbose_name='役割')),
            ],
            options={
                'verbose_name': '参画研究者',
                'verbose_name_plural': '参画研究者',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('source', models.CharField(choices=[('1', 'KAKEN'), ('2', 'JSTDB'), ('3', 'WoS')], max_length=1, verbose_name='取得元')),
                ('pid', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='永続的識別子')),
                ('category', models.CharField(max_length=255, verbose_name='種別')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('year', models.IntegerField(verbose_name='開始年度／公表年')),
                ('keywords', models.ManyToManyField(to='work.Keyword')),
                ('members', models.ManyToManyField(to='work.Member')),
            ],
            options={
                'verbose_name': '研究業績',
                'verbose_name_plural': '研究業績',
            },
        ),
    ]
