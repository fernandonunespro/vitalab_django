# Generated by Django 4.2.6 on 2023-10-10 19:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exames', '0003_pedidosexames'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PedidosExames',
            new_name='PedidosExame',
        ),
        migrations.RenameModel(
            old_name='TiposExames',
            new_name='TiposExame',
        ),
    ]
