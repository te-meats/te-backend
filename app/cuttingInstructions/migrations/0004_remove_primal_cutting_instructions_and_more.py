# Generated by Django 4.2.3 on 2024-11-13 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuttingInstructions', '0003_remove_cuttinginstruction_primals_remove_primal_cuts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primal',
            name='cutting_instructions',
        ),
        migrations.AddField(
            model_name='primal',
            name='cutting_instruction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primals', to='cuttingInstructions.cuttinginstruction'),
        ),
        migrations.AlterField(
            model_name='cut',
            name='primal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuts', to='cuttingInstructions.primal'),
        ),
    ]