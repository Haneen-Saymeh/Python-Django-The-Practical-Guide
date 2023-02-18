# Generated by Django 4.1.6 on 2023-02-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0005_address_alter_book_author_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'address entries'},
        ),
        migrations.AddField(
            model_name='book',
            name='countries',
            field=models.ManyToManyField(related_name='books', to='book_store.country'),
        ),
    ]