# Generated by Django 4.1.7 on 2023-03-20 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_point',
            name='parent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Menu.menu_point'),
        ),
    ]
