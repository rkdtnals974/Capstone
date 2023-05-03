# Generated by Django 4.2 on 2023-05-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_accounts_userpw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='username',
            field=models.TextField(max_length=64, verbose_name='사용자명'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='userpw',
            field=models.TextField(max_length=128, verbose_name='사용자비밀번호'),
        ),
    ]
