# Generated by Django 4.1.3 on 2022-12-15 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('byebnk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aplicacao',
            old_name='preco_unitario',
            new_name='preco_unitario_a',
        ),
        migrations.RenameField(
            model_name='aplicacao',
            old_name='quantidade_ativos',
            new_name='quantidade_ativos_a',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='preco_unitario',
            new_name='preco_unitario_r',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='quantidade_ativos',
            new_name='quantidade_ativos_r',
        ),
    ]
