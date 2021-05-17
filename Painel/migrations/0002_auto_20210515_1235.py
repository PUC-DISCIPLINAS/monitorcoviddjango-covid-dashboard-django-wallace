# Generated by Django 3.2.2 on 2021-05-15 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Painel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='country',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Painel.country'),
        ),
    ]
