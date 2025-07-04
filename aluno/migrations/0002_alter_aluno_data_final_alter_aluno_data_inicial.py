# Generated by Django 5.2.1 on 2025-06-06 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_final',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 6, 6, 22, 51, 47, 439659, tzinfo=datetime.timezone.utc), help_text='Informe a data final de matrícula do Aluno', null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 6, 6, 22, 51, 47, 439659, tzinfo=datetime.timezone.utc), help_text='Informe a data inicial de matrícula do Aluno'),
        ),
    ]
