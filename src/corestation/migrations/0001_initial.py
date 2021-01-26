# Generated by Django 3.1.4 on 2021-01-13 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attached_to', models.CharField(max_length=50, verbose_name='附置組織')),
                ('name', models.CharField(max_length=255, verbose_name='事業体名')),
                ('date_of_establishment', models.DateField(verbose_name='設立年月日')),
            ],
            options={
                'verbose_name': 'コア・ステーション',
                'verbose_name_plural': 'コア・ステーション',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eradcode', models.CharField(blank=True, max_length=8, null=True, verbose_name='研究者番号')),
                ('shimei', models.CharField(max_length=50, verbose_name='氏名')),
                ('shozoku', models.CharField(max_length=50, verbose_name='所属')),
                ('specialized_field', models.CharField(max_length=200, verbose_name='専門分野')),
                ('is_representative', models.CharField(choices=[('0', ''), ('1', '事業代表者')], max_length=1, verbose_name='事業代表者')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='corestation.station')),
            ],
            options={
                'verbose_name': '構成員',
                'verbose_name_plural': '構成員',
            },
        ),
    ]
