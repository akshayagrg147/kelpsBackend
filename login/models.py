from django.db import models
from home_screen.models import TblAddress


class TblUser(models.Model):
    email = models.CharField(max_length=255)
    full_name = models.CharField(max_length=75)
    password = models.CharField(max_length=255)
    salt_key = models.CharField(max_length=255)
    user_type = models.IntegerField()
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    created_on = models.DateTimeField()
    created_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    gst_number = models.CharField(max_length=100, blank=True, null=True)
    shipping_address = models.ForeignKey(TblAddress, models.DO_NOTHING, db_column='shipping_address', blank=True, null=True, related_name='ship')
    billing_address = models.ForeignKey(TblAddress, models.DO_NOTHING, db_column='billing_address', blank=True, null=True, related_name='bill')
    gst_information = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user'


class TblUserType(models.Model):
    type_name = models.CharField(max_length=75)
    type_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_type'