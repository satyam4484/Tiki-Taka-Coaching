# Generated by Django 3.2.6 on 2021-09-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0008_alter_parentdata_playername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerdata',
            name='PlayerCellNumber',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]