# Generated by Django 4.1.4 on 2022-12-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
