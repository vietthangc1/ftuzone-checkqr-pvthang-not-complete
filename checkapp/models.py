from django.db import models
from datetime import datetime
import uuid

from django.db.models.fields import EmailField

# Create your models here.
class Customers(models.Model):
  user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256)
  CardId = models.CharField(max_length=20, blank=True)
  YearofBirth = models.IntegerField(blank=True)
  email = models.EmailField(default="@gmail.com")
  phone = models.CharField(max_length=15, blank=True)
  school = models.CharField(max_length=256)
  created_time = models.DateTimeField(default=datetime.now, editable=False)
  times_of_scan = models.IntegerField(default=0, editable=False)
  last_scanned = models.DateTimeField(blank=True, null=True)

  @property
  def qr_link(self):
      "Returns the link of qr code for user_id."
      return "http://127.0.0.1:8000/app/scan/"+str(self.user_id)
      # return "https://ftuzone-checkqr-pvthang.herokuapp.com/app/scan/"+str(self.user_id)

  def __str__(self):
    return self.name