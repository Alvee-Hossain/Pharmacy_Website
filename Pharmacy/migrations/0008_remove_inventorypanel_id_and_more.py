# Generated by Django 4.1.1 on 2022-12-14 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacy', '0007_inventorypanel_alter_employeepanel_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorypanel',
            name='id',
        ),
        migrations.AlterField(
            model_name='inventorypanel',
            name='medicine',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
