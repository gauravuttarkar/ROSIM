# Generated by Django 3.0.3 on 2020-03-12 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200312_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Clients', unique=True),
        ),
    ]