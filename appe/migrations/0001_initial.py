# Generated by Django 2.1.4 on 2019-07-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_details',
            fields=[
                ('USERNAME', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('PASSWORD', models.CharField(max_length=150)),
                ('EMAIL', models.EmailField(max_length=150)),
                ('MOBILENO', models.CharField(max_length=10)),
            ],
        ),
    ]
