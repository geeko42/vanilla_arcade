# Generated by Django 2.0.4 on 2018-12-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0026_auto_20181228_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=128, null=True),
        ),
    ]
