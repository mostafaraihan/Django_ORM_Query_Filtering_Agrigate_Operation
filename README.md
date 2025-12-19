# 🚀 Django Invoice & Inventory Management System

A **fully-featured Django backend project** demonstrating **advanced ORM queries**, **relational database design**, **JSON APIs**, and **real-world invoice & billing logic**.

This project is designed for **learning, interviews, and production-style architecture**.

---

## 📌 Key Features

✅ Custom User Model  
✅ Category & Product Management  
✅ Customer & Invoice System  
✅ Invoice–Product Relationship  
✅ Advanced Django ORM Queries  
✅ Aggregations & Analytics  
✅ Optimized Database Access  
✅ Clean JSON API Responses  


---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Django 6 |
| Language | Python 3.13.3 |
| Database | SQLite |
| ORM | Django ORM |
| API Type | JsonResponse |


---

## 🧩 Database Models

### 🔐 User Model

```python
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=500)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
📦 Product Model
```
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
```
👤 Customer Model
```
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
```
🧾 Invoice Model
```
class Invoice(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_due = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
```
🧮 InvoiceProduct Model
```
class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
```

⚙️ Advanced ORM Examples
🔍 Filtering & Sorting
```
User.objects.filter(username__icontains='ra')
User.objects.exclude(username__icontains='ra')
User.objects.order_by('username')
User.objects.order_by('-username')
```

📏 Comparison Operators
```
Product.objects.filter(price__gt=500)
Product.objects.filter(price__lt=500)
Product.objects.filter(price__range=(200, 500))
Product.objects.filter(price__in=[100, 500])
```
🔀 Complex Queries (Q Objects)
```
from django.db.models import Q

Product.objects.filter(
    Q(name__icontains='a') |
    Q(price__gt=500)
)
```
---





