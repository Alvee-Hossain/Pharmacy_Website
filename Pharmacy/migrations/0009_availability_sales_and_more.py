# Generated by Django 4.1.1 on 2022-12-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacy', '0008_remove_inventorypanel_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('drug_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('drug_group', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('availability', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sale', models.CharField(max_length=100)),
                ('monthly_sale', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='inventorypanel',
            old_name='medicine',
            new_name='drug_name',
        ),
    ]