from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "نام دسته‌بندی")
    slug = models.SlugField(max_length=100, allow_unicode=True, verbose_name = "اسلاگ")
    order = models.PositiveIntegerField(default=5, verbose_name="اولویت نمایش")
    def __str__(self):
        return self.name

    def get_last_items(self):
        items = Item.objects.filter(cat = self)
        return items[:6]

    def get_item_count(self):
        return Item.objects.filter(cat=self).count()
    get_item_count.short_description = "تعداد محصولات"

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی'
        ordering = ('order', 'name',)

class Item(models.Model):
    created = models.DateTimeField(default = timezone.now, verbose_name = "زمان ایجاد")
    title = models.CharField(max_length=255, verbose_name = "نام محصول")
    slug = models.SlugField(allow_unicode=True, verbose_name = "اسلاگ")
    image = models.ImageField(upload_to = "images/items/", verbose_name = "تصویر محصول")
    is_offer = models.BooleanField(default = False, verbose_name = "مشاهده در صفحه اصلی")
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items",verbose_name = "دسته‌بندی")
    views = models.PositiveIntegerField(default=0, verbose_name = "تعداد بازدید")
    body = HTMLField(blank = True, null = True,verbose_name = "بدنه ")
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ('-created',)



class Company(models.Model):
    image = models.ImageField(upload_to='images/item/', blank=True, null=True, verbose_name="تصویر  (۲۰۰ در ۱۵۰)")
    name = models.CharField(max_length=255, verbose_name = "نام")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'طرف قرارداد'
        verbose_name_plural = 'طرف قراردادها'
        ordering = ('name',)


class UserMessage(models.Model):
    created = models.DateTimeField(default = timezone.now,verbose_name = 'زمان ایجاد')
    name = models.CharField(max_length=100, verbose_name = "نام")
    subject = models.CharField(max_length=100, verbose_name = "موضوع")
    phone = models.CharField(max_length=100, verbose_name = "شماره تماس")
    message = models.TextField(verbose_name = "پیام")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام‌ها"
        ordering =("-created",)


class GalleryImage(models.Model):
    created = models.DateTimeField(default = timezone.now,verbose_name = 'زمان ایجاد')
    name = models.CharField(max_length=100, verbose_name = "نام")
    image = models.ImageField(upload_to = 'images/gallereis/', verbose_name = 'تصویر (1200x900)')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "عکس گالری"
        verbose_name_plural = "عکس‌های گالری"
        ordering =("-created",)

