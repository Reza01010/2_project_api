# Generated by Django 4.2.1 on 2023-05-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0004_alter_cryptocurrency1_usd_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency1',
            name='usd_price',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=20, null=True),
        ),
    ]
