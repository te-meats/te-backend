# Generated by Django 4.2.3 on 2024-11-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('cutType', models.CharField()),
                ('prepType', models.CharField()),
                ('quantity', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Primal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('cuts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuttingInstructions.cut')),
            ],
        ),
        migrations.CreateModel(
            name='CuttingInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('primals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuttingInstructions.primal')),
            ],
        ),
    ]
