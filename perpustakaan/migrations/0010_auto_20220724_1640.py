# Generated by Django 3.0.5 on 2022-07-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0009_auto_20220724_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='cover',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media/'),
        ),
        migrations.AlterModelTable(
            name='buku',
            table='myapp_image',
        ),
    ]