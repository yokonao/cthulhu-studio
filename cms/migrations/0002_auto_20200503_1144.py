# Generated by Django 3.0.5 on 2020-05-03 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='age',
        ),
        migrations.RemoveField(
            model_name='character',
            name='background',
        ),
        migrations.RemoveField(
            model_name='character',
            name='birthplace',
        ),
        migrations.RemoveField(
            model_name='character',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='character',
            name='profession',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(blank=True, max_length=255, null=True, verbose_name='職業')),
                ('background', models.CharField(blank=True, max_length=255, null=True, verbose_name='学校・学位')),
                ('birthplace', models.CharField(blank=True, max_length=255, null=True, verbose_name='出身')),
                ('gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='性別')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年齢')),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.Character', verbose_name='キャラクター')),
            ],
        ),
    ]
