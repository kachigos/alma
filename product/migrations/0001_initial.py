# Generated by Django 4.1 on 2022-08-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('categories', models.ManyToManyField(related_name='products', to='product.category')),
            ],
        ),
    ]