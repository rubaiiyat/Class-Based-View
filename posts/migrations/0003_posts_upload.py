# Generated by Django 5.0.7 on 2024-10-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='posts/media/uploads/'),
        ),
    ]
