# Generated by Django 4.1.5 on 2023-01-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_category_slug_alter_subcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.CharField(default=1, max_length=500, unique=True),
            preserve_default=False,
        ),
    ]