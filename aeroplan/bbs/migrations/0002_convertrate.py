# Generated by Django 5.1 on 2024-09-20 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='convertRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=100)),
                ('arrival', models.CharField(max_length=100)),
                ('航班时间', models.DateField(blank=True, null=True)),
                ('积分', models.BigIntegerField()),
                ('现金', models.BigIntegerField()),
                ('convertRate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
