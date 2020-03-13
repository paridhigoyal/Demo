# Generated by Django 2.2.11 on 2020-03-09 09:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False, verbose_name='customer status')),
                ('is_transporter', models.BooleanField(default=False, verbose_name='transporter status')),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=30)),
                ('state', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=12)),
                ('pin_code', models.CharField(default='', max_length=6)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('deal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_Date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_city', models.CharField(max_length=50)),
                ('end_city', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('unit', models.CharField(default='Rs', max_length=5)),
                ('transporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QueryRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_request', models.TextField(default='')),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation_deal.Deal')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(default='', max_length=50)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=15)),
                ('man_Year', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('unit', models.CharField(default='kgs', max_length=5)),
                ('picture', models.ImageField(null=True, upload_to='gallery')),
                ('document', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
                ('transporter', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 'Worst Experience'), ('2', 'Bad Experience'), ('3', 'Good Experience'), ('4', 'Very Good Experience'), ('5', 'Excellent Experience')], max_length=1)),
                ('deal_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transportation_deal.Deal')),
                ('transporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QueryResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_response', models.TextField(default='')),
                ('request_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transportation_deal.QueryRequest')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='vehicle_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transportation_deal.Vehicle'),
        ),
    ]