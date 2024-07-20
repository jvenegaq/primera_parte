# Generated by Django 5.0.6 on 2024-07-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='fundacion',
        ),
        migrations.AddField(
            model_name='equipo',
            name='color_camiseta',
            field=models.CharField(default='color_camiseta', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='hinchada',
            field=models.CharField(default='color_camiseta', max_length=100),
            preserve_default=False,
        ),
    ]
