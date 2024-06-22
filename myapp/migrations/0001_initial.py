# Generated by Django 4.2.13 on 2024-06-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
                ('dod', models.DateField(auto_now=True)),
            ],
        ),
    ]