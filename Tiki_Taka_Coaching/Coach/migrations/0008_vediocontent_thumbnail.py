# Generated by Django 3.2.6 on 2021-10-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coach', '0007_alter_vediocontent_vedio'),
    ]

    operations = [
        migrations.AddField(
            model_name='vediocontent',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='images/%y'),
            preserve_default=False,
        ),
    ]
