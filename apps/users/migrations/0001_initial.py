# Generated by Django 4.2.6 on 2023-10-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
                'ordering': ['id'],
            },
        ),
    ]

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

