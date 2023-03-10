# Generated by Django 2.2.5 on 2023-01-15 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exceldata',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('article', models.CharField(max_length=100)),
                ('pairs', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'db_table': 'excel_data',
            },
        ),
    ]
