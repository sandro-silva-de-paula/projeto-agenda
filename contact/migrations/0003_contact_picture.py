# Generated by Django 5.0.1 on 2024-02-03 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_show_alter_contact_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m', verbose_name='Foto'),
        ),
    ]