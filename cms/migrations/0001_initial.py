# Generated by Django 3.0.5 on 2020-05-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('profession', models.CharField(blank=True, max_length=255, null=True, verbose_name='職業')),
                ('background', models.CharField(blank=True, max_length=255, null=True, verbose_name='学校・学位')),
                ('birthplace', models.CharField(blank=True, max_length=255, null=True, verbose_name='出身')),
                ('gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='性別')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年齢')),
                ('strength', models.IntegerField(default=9, verbose_name='STR')),
                ('constitution', models.IntegerField(default=9, verbose_name='CON')),
                ('size', models.IntegerField(default=9, verbose_name='SIZ')),
                ('dexterity', models.IntegerField(default=9, verbose_name='DEX')),
                ('appearance', models.IntegerField(default=9, verbose_name='APP')),
                ('intelligence', models.IntegerField(default=9, verbose_name='INT')),
                ('power', models.IntegerField(default=9, verbose_name='POW')),
                ('education', models.IntegerField(default=12, verbose_name='EDU')),
                ('idea', models.IntegerField(default=50, verbose_name='アイデア')),
                ('luck', models.IntegerField(default=50, verbose_name='幸運')),
                ('knowledge', models.IntegerField(default=50, verbose_name='知識')),
                ('sanity_point', models.IntegerField(default=50, verbose_name='SAN値')),
                ('max_sanity_point', models.IntegerField(default=99, verbose_name='最大正気度')),
                ('magic_point', models.IntegerField(default=9, verbose_name='マジックポイント')),
                ('durability', models.IntegerField(default=9, verbose_name='耐久力')),
                ('damage_bonus', models.CharField(default='0', max_length=10, verbose_name='ダメージ・ボーナス')),
            ],
        ),
    ]
