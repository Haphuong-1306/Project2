# Generated by Django 2.2.7 on 2019-11-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_orderdetail_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Đã giao hàng', max_length=255),
            preserve_default=False,
        ),
    ]
