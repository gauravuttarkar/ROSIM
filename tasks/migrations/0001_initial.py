# Generated by Django 3.0.3 on 2020-02-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('mac', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=20, null=True)),
            ],
        ),
    ]
