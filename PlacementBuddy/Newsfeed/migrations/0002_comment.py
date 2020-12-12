# Generated by Django 3.1.3 on 2020-12-12 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20201211_1317'),
        ('Newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Newsfeed.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.user')),
            ],
        ),
    ]
