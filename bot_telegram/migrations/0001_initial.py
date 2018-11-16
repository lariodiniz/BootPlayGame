# Generated by Django 2.1.3 on 2018-11-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('iniciou', models.DateTimeField(auto_now_add=True, verbose_name='Iniciou')),
                ('ultimo_acesso', models.DateTimeField(auto_now=True, verbose_name='Ultimo Acesso')),
            ],
        ),
    ]
