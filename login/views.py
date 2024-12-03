from django.shortcuts import render
from rest_framework.decorators import api_view
from health_care.response import JsendSuccessResponse
from .service import login_check, register_user, user_info_logic, gst_number_verification
from health_care import constants

@api_view(['POST'])
def user_register(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_REGISTER_API)
    
    data = request.data
    status, response_data, message = register_user(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['POST'])
def user_login(request):
    print(constants.BREAKCODE)
    print(constants.INITIATED_LOGIN_API)

    data = request.data
    status, response_data, message = login_check(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def user_info(request):
    print(constants.BREAKCODE)
    print(constants.INITIATED_USER_INFO_API)

    data = request.query_params
    user_id = data['user_id'] if 'user_id' in data else None
    status, response_data, message = user_info_logic(user_id)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()


@api_view(['GET'])
def gst_verification(request):
    print(constants.BREAKCODE)
    print(constants.INITIATED_GET_VERIFICATION)

    data = request.query_params
    gst_number = data.get('gst_number')
    pincode = data.get('pincode')
    
    status, response_data, message = gst_number_verification(gst_number, pincode)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()