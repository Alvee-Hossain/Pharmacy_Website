# Generated by Django 4.1.1 on 2022-12-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacy', '0005_alter_employeepanel_id_alter_employeepanel_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeepanel',
            name='ID',
        ),
        migrations.AlterField(
            model_name='employeepanel',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
