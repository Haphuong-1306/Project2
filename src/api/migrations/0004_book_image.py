# Generated by Django 2.2.7 on 2019-11-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191118_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to='photos'),
            preserve_default=False,
        ),
    ]