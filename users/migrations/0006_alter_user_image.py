# Generated by Django 4.1.4 on 2022-12-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_contacts_alter_user_image_delete_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='media/default-profile.jpg', null=True, upload_to=''),
        ),
    ]