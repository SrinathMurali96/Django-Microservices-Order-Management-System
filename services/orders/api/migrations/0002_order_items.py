# Generated by Django 2.0.2 on 2018-03-24 21:03

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=djongo.models.fields.ListField(default=None),
        ),
    ]
