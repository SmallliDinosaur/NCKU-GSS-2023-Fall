# Generated by Django 4.2.5 on 2023-10-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaur', '0007_delete_timeslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
