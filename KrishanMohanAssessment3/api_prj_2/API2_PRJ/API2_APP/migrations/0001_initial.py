# Generated by Django 5.1.6 on 2025-02-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
    ]
