# Generated by Django 4.2 on 2024-09-02 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_alter_mailingtry_options_remove_mailing_clients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='start_date',
        ),
    ]
