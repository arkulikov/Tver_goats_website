# Generated by Django 4.0.3 on 2022-04-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_grip_options_alter_role_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_number',
            field=models.CharField(default='00', max_length=2, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='grip',
            name='grip',
            field=models.CharField(max_length=10, verbose_name='Хват'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='player',
            name='surname',
            field=models.CharField(max_length=50, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=15, verbose_name='Амплуа'),
        ),
    ]
