# Generated by Django 3.1.3 on 2020-11-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20201117_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]
