# Generated by Django 4.2.2 on 2023-07-01 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabla1',
            name='campo2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla1',
            name='campo3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla2',
            name='campo1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla2',
            name='campo2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla2',
            name='campo3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla3',
            name='campo1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla3',
            name='campo2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tabla3',
            name='campo3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='tabla1',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tabla2',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tabla3',
            table=None,
        ),
        migrations.AlterModelTable(
            name='usuario',
            table=None,
        ),
    ]