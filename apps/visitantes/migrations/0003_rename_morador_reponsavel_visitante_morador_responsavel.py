# Generated by Django 5.0.1 on 2024-01-24 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_visitante_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitante',
            old_name='morador_reponsavel',
            new_name='morador_responsavel',
        ),
    ]
