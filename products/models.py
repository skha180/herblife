from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # NEW: for blog URLs
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # optional
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.name} - {self.product.title} ({self.status})"


# --- New model for blog content ---
class BlogPost(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, blank=True, default="")
    content = models.TextField()  # blog HTML content
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.product.title})"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_detail', args=[self.slug])
