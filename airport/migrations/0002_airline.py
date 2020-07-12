# Generated by Django 2.1.5 on 2020-04-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alid', models.CharField(max_length=20)),
                ('alname', models.CharField(max_length=100)),
                ('apcountry', models.CharField(max_length=100)),
                ('apIATA', models.CharField(max_length=100)),
                ('apICAO', models.CharField(max_length=100)),
                ('apstate', models.TimeField(max_length=100)),
                ('ap_nooflights', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'airline',
            },
        ),
    ]