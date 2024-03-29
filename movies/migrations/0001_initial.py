# Generated by Django 5.0.2 on 2024-03-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=200)),
            ],
        ),
    ]
