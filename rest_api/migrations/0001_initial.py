# Generated by Django 2.2.4 on 2019-08-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=250, unique=True)),
                ('bank_id', models.IntegerField(blank=True, null=True)),
                ('branch', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('district', models.CharField(blank=True, max_length=250, null=True)),
                ('state', models.CharField(blank=True, max_length=250, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
