# Generated by Django 4.2.3 on 2024-11-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuttingInstructions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuttinginstruction',
            name='primals',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cuttingInstructions.primal'),
        ),
        migrations.AlterField(
            model_name='primal',
            name='cuts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cuttingInstructions.cut'),
        ),
    ]
