# Generated by Django 4.2.4 on 2023-08-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=10, unique=True)),
                ('bank_name', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
