# Generated by Django 3.2.2 on 2021-05-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Painel', '0002_auto_20210515_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]