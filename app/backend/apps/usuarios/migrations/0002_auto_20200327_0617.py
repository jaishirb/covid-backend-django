# Generated by Django 2.2 on 2020-03-27 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Rol usuario',
                'verbose_name_plural': 'Rol usuarios',
            },
        ),
        migrations.AddField(
            model_name='usuariocovid',
            name='rol_usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.RolUsuario'),
            preserve_default=False,
        ),
    ]
