# Generated by Django 4.2.5 on 2023-10-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaur', '0005_alter_conferoom_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
                ('monday', models.CharField(max_length=255)),
                ('tuesday', models.CharField(max_length=255)),
                ('wednesday', models.CharField(max_length=255)),
                ('thursday', models.CharField(max_length=255)),
                ('friday', models.CharField(max_length=255)),
            ],
        ),
    ]
