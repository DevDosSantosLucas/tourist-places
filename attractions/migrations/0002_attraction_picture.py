# Generated by Django 3.2.16 on 2023-02-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='attractions'),
        ),
    ]