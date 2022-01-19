# Generated by Django 4.0.1 on 2022-01-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=200)),
                ('pin_code', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]