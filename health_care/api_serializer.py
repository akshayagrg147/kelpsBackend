from rest_framework import serializers

class user_register_serializer(serializers.Serializer):
    email       = serializers.CharField()  
    name        = serializers.CharField()  
    password    = serializers.CharField()
    state       = serializers.CharField()  
    district    = serializers.CharField()  

class user_login_serializer(serializers.Serializer):
    email       = serializers.CharField(max_length = 255)
    password    = serializers.CharField(max_length = 255)

class order_place_serializer(serializers.Serializer):
    user_id     = serializers.IntegerField()
    price       = serializers.CharField(max_length = 255)
    products    = serializers.JSONField()
    
class address_update_serializer(serializers.Serializer):
    user_id     = serializers.IntegerField()
    address_id  = serializers.IntegerField()
    
class add_products_serializer(serializers.Serializer):
    name                 = serializers.CharField()