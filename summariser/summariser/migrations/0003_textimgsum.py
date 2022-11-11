# Generated by Django 4.0.4 on 2022-11-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summariser', '0002_pythonsum'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextImgSum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(upload_to='summariser/files/imgs')),
            ],
        ),
    ]
