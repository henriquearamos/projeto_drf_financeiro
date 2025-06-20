# Generated by Django 5.2.3 on 2025-06-15 15:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now=True)),
                ('nome_fonte', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Fonte',
                'verbose_name_plural': 'Fontes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now=True)),
                ('data', models.DateField()),
                ('tipo_entrada', models.CharField(choices=[('desconto', 'Desconto'), ('credito', 'Crédito')], max_length=10)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fonte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transacoes.fonte')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transação',
                'verbose_name_plural': 'Transações',
                'ordering': ['id'],
            },
        ),
    ]
