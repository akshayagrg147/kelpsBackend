from rest_framework.decorators import api_view
from rest_framework.views import APIView
from health_care.response import JsendSuccessResponse
from health_care import constants
from home_screen.service import product_info_logic
from .services import get_sub_category, add_sub_category, update_sub_category, delete_sub_category, get_products, add_products, update_products, delete_product, get_category, add_category, update_category, delete_category, get_orgs, add_orgs, update_orgs, delete_orgs, product_search_logic, organization_search_logic, sub_category_search_logic, category_search_logic
import json


class Category(APIView):
    def get(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_CATEGORY_FETCH)
        
        
        data = request.query_params
        user_id = data['user_id'] if 'user_id' in data else None
        
        status, response_data, message = get_category(user_id=user_id)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def post(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_CATEGORY_ADD)
        
        data = request.body
        
        data = json.loads(data)
        
        user_id = data.get('user_id')
        categories = data['categories']
                
        status, response_data, message = add_category(user_id, categories)
        
        return JsendSuccessResponse(status = status,data = response_data, message=str(message)).get_response()
    
    def patch(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_CATEGORY_UPDATE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = update_category(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def delete(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_CATEGORY_DELETE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = delete_category(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
class Organisation(APIView):
    def get(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_ORGANIZATION_FETCH)
        
        
        data = request.query_params
        
        status, response_data, message = get_orgs(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def post(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_ORGANIZATION_ADD)
        
        data = request.body
        
        data = json.loads(data)
        
        user_id = data.get('user_id')
        organization_object = data.get('organizations')
                
        status, response_data, message = add_orgs(organization_object)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def patch(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_ORGANIZATION_UPDATE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = update_orgs(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def delete(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_ORGANIZATION_DELETE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = delete_orgs(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
        
class Sub_Category(APIView):
    def get(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_SUB_CATEGORY_FETCH)
        
        data = request.query_params
                
        status, response_data, message = get_sub_category(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response() 
    
    def post(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_SUB_CATEGORY_ADD)
        
        data = request.body
        
        data = json.loads(data)
        
        user_id = data.get('user_id')
        organization_object = data['sub_category']
                
        status, response_data, message = add_sub_category(user_id, organization_object)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response() 
    
    def patch(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_SUB_CATEGORY_UPDATE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = update_sub_category(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response() 
    
    def delete(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_SUB_CATEGORY_DELETE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = delete_sub_category(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response() 
    
class Products(APIView):
    def get(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_PRODUCTS_FETCH)
        
        data = request.query_params
        
        status, response_data, message = get_products(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def post(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_PRODUCTS_ADD)
        
        data = request.body
        
        data = json.loads(data)
        
        user_id = data.get('user_id')
        products_object = data['products']
                
        status, response_data, message = add_products(user_id, products_object)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def patch(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_PRODUCTS_UPDATE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = update_products(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    
    def delete(self, request, *args, **kwargs):
        print(constants.BREAKCODE)
        print(constants.INITIATED_PRODUCTS_DELETE)
        
        data = request.body
        
        data = json.loads(data)
                
        status, response_data, message = delete_product(data)
        
        return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
        

@api_view(['GET'])
def product_search(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_PRODUCT_SEARCH_API)
    
    data = request.query_params
    
    status, response_data, message = product_search_logic(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def organization_search(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_ORGANIZATION_SEARCH_API)
    
    data = request.query_params
    
    status, response_data, message = organization_search_logic(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def sub_category_search(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_SUB_CATEGORY_SEARCH_API)
    
    data = request.query_params
    
    status, response_data, message = sub_category_search_logic(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def category_search(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_CATEGORY_SEARCH_API)
    
    data = request.query_params
    
    status, response_data, message = category_search_logic(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def Category_info(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_CATEGORY_SEARCH_API)
    
    data = request.query_params
    
    category_id = data.get('category_id')
    
    status, response_data, message = get_category(category_id=category_id)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def product_info(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_PRODUCT_INFO_API)
    
    data = request.query_params
    
    product_id = data.get('id')
    
    status, response_data, message = product_info_logic(product_id = product_id, flag = 'internal')
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
        
 
 
      