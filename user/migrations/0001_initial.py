# Generated by Django 2.0.1 on 2019-03-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('birday', models.DateTimeField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('address', models.CharField(default='', max_length=200, verbose_name='地址')),
                ('mobile', models.CharField(blank=True, max_length=100, null=True, verbose_name='手机号')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%M', verbose_name='图片')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
