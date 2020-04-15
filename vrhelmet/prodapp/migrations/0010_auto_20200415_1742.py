# Generated by Django 3.0.4 on 2020-04-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodapp', '0009_auto_20200415_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('text', models.CharField(max_length=300)),
                ('tel', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
