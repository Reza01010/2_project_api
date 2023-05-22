# Generated by Django 4.2.1 on 2023-05-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency1',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='cryptocurrency1',
            name='usd_price',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=200, null=True),
        ),
    ]
