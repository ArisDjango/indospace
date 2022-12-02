from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_admin_filters import MultiChoice

COLOR = (
  ('RD', 'Red'),
  ('BU', 'Blue'),
  ('GR', 'Green'),
)

# FAMILY = (
#   ('FU', 'Furniture'),
#   ('WS', 'Workspace'),
#   ('OT', 'Outdoor Products'),
# )

# CHANNEL = (
#   ('EC', 'E-Commerce'),
#   ('MO', 'Mobile'),
#   ('PR', 'Print'),
# )


class Channel(models.Model):
    name = models.CharField(max_length=200, default='E-Commerce')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'channel'
        verbose_name_plural = 'channels'

    def __str__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(max_length=200, default='Furniture')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'family'
        verbose_name_plural = 'families'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_family', args=[self.slug])

class Materials(models.Model):
    label = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    

    class Meta:
        ordering = ['label']
        indexes = [
            models.Index(fields=['label']),
        ]
        

    def __str__(self):
        return self.label

class Category(models.Model):
    family = models.ForeignKey(Family,
                                related_name = 'categories',
                                on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    channel = models.ForeignKey(Channel,
                                related_name='products_channel',
                                on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category,
                related_name='products',
                on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_tech = models,models.ImageField(upload_to='products/technique', height_field=None, width_field=None, max_length=None, blank=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=2, default='RD', choices=COLOR)
    material = models.ForeignKey(Materials, 
                                    related_name='material_products',
                                    on_delete=models.CASCADE,
                                    null=True)
    width = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight_gross = models.IntegerField(blank=True, null=True)
    weight_net = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    package = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['image']),
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
            
        ]

    def __str__(self):
        return self.name

    # def img_preview(self): #new
    #     return mark_safe('<img scr = "{}" witdh = "800"/>'.format(self.image.url))
    # img_preview.short_description = 'Image'
    # img_preview.allow_tags = True

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

