# Generated by Django 4.1 on 2024-06-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/default/default_profile.png', null=True, upload_to='images/profile/'),
        ),
    ]
