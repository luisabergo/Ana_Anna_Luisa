# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100, db_index=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='nome',
            new_name='matricula',
        ),
        migrations.RenameField(
            model_name='disciplina',
            old_name='nome',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='nome',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='horario',
            field=models.CharField(max_length=100, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='nome_disc',
            field=models.CharField(max_length=100, db_index=True, default=datetime.datetime(2021, 2, 3, 2, 40, 2, 932702, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='phone',
            field=models.IntegerField(max_length=15, default=datetime.datetime(2021, 2, 3, 2, 40, 19, 302040, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='pontuacao',
            field=models.FloatField(),
        ),
    ]
