# Generated by Django 3.2.6 on 2021-10-02 12:41

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Coach', '0005_auto_20211001_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vediocontent',
            name='vedio',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
