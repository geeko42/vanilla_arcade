# Generated by Django 2.0.4 on 2018-12-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20181218_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitelogo',
            name='image',
            field=models.ImageField(upload_to='vanilla_arcade/media', verbose_name='img'),
        ),
    ]