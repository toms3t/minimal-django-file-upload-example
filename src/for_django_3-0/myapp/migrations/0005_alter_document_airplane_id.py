# Generated by Django 3.2.4 on 2021-06-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_document_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='airplane_id',
            field=models.CharField(default='1', max_length=200),
        ),
    ]
