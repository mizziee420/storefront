# Generated by Django 3.2.7 on 2021-09-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_alter_tag_attached_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='attached_file',
            field=models.FileField(upload_to='tags'),
        ),
    ]
