# Generated by Django 4.1.5 on 2023-02-12 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_product_slug_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
                ('slug', models.CharField(max_length=500)),
            ],
        ),
    ]
