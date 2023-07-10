# Generated by Django 3.2 on 2022-10-01 07:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دسته\u200cبندی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, verbose_name='اسلاگ')),
                ('image', models.ImageField(upload_to='images/subcat/', verbose_name='تصویر دسته\u200cبندی')),
                ('order', models.PositiveIntegerField(default=5, verbose_name='اولویت نمایش')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی',
                'ordering': ('order', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/item/', verbose_name='تصویر (۲۰۰ در ۷۰)')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'طرف قرارداد',
                'verbose_name_plural': 'طرف قراردادها',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('image', models.ImageField(upload_to='images/gallery/', verbose_name='تصویر (1200x900)')),
            ],
            options={
                'verbose_name': 'عکس گالری',
                'verbose_name_plural': 'عکس\u200cهای گالری',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('subject', models.CharField(max_length=100, verbose_name='موضوع')),
                ('phone', models.CharField(max_length=100, verbose_name='شماره تماس')),
                ('message', models.TextField(verbose_name='پیام')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام\u200cها',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('title', models.CharField(max_length=255, verbose_name='نام محصول')),
                ('slug', models.SlugField(allow_unicode=True, verbose_name='اسلاگ')),
                ('image', models.ImageField(upload_to='images/items/', verbose_name='تصویر محصول')),
                ('is_offer', models.BooleanField(default=False, verbose_name='مشاهده در صفحه اصلی')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')),
                ('body', tinymce.models.HTMLField(blank=True, null=True, verbose_name='بدنه ')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.category', verbose_name='دسته\u200cبندی')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
                'ordering': ('-created',),
            },
        ),
    ]
