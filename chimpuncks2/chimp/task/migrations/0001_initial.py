# Generated by Django 5.0.3 on 2024-05-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resolve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50, verbose_name='ID задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID задачи')),
                ('name', models.CharField(max_length=50, verbose_name='ID задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50, verbose_name='ID задачи')),
            ],
        ),
    ]
