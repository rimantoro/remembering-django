# Generated by Django 2.1.15 on 2020-09-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_type', models.CharField(default=None, help_text='goods type name', max_length=50, unique=True, verbose_name='goods_type')),
                ('temp_min', models.IntegerField(help_text='minimum temperature threshold in celcius', verbose_name='temp_min')),
                ('temp_max', models.IntegerField(help_text='maximum temperature threshold in celcius', verbose_name='temp_max')),
            ],
            options={
                'ordering': ['goods_type'],
            },
        ),
    ]
