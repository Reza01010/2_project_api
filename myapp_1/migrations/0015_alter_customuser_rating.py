# Generated by Django 4.2.1 on 2023-05-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0014_alter_cryptocurrency2_response_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Rating',
            field=models.CharField(choices=[('G', 'Gold'), ('s', 'silver')], default='S', max_length=10),
        ),
    ]
