from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length = 255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'P', 'Pending'
        CHINESE = 'Cm', 'Completed'
        ITALIAN = 'Cn', 'Canceled'
    
    po_number = models.CharField(max_length = 255)
    vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    order_date = models.DateTimeField(auto_now_add = True)
    # items = models.JSONField(blank = True, default = '')
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length = 2, choices = TypeChoices.choices)
    quality_rating = models.PositiveIntegerField()
    issue_date = models.DateTimeField(auto_now = False, null = True)
    acknowledgment_date = models.DateTimeField(auto_now = False, null = True)

    def __str__(self):
        return f" order from {self.vendor} of quantity {self.quantity}  "


