# Generated by Django 4.2.1 on 2023-05-30 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorInferencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=110),
        ),
    ]
