# Generated by Django 5.0.4 on 2024-04-18 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_subscription_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fake_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('duration', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('comment_count', models.IntegerField()),
            ],
        ),
    ]
