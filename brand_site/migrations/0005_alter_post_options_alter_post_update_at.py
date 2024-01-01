# Generated by Django 4.2.8 on 2024-01-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_site', '0004_alter_post_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-update_at',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='update time'),
        ),
    ]
