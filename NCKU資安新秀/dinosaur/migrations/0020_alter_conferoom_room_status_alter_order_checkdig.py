# Generated by Django 4.2.7 on 2023-11-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaur', '0019_alter_conferoom_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferoom',
            name='room_status',
            field=models.CharField(default='✔️', max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='checkdig',
            field=models.CharField(default='未到', max_length=4),
        ),
    ]
