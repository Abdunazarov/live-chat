# Generated by Django 4.1.4 on 2022-12-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
