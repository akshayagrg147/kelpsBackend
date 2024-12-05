from rest_framework.decorators import api_view
from health_care.response import JsendSuccessResponse
from health_care import constants
from .service import home_screen_logic, product_info_logic,sub_catproduct_info_logic, product_info_list_logic, address_insertion_logic, address_updation_logic, search_functionality_logic, get_states, get_district, get_organizations, rating_update_logic
from admin_pages.services import get_category
import json

@api_view(['GET'])
def home_screen_info(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_HOME_SCREEN_API)
    
    data = request.query_params
    user_id = data['user_id'] if 'user_id' in data else None
    
    status, response_data, message = home_screen_logic(user_id)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def home_sub_category_product_info(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_SUBCAT_PRODUCT_API)
    
    data = request.query_params
    
    status, response_data, message = sub_catproduct_info_logic(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['POST'])
def product_info_list(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_SUBCAT_PRODUCT_API)
    
    status = 'Error'
    response_data = None
    message = "Invalid params"
    data = request.body
    
    if data:
        data = data.decode("utf-8")
        
        data = json.loads(data)
    
    product_ids = data['ids'] if 'ids' in data else None
    
    if product_ids and isinstance(product_ids, list):
        status, response_data, message = product_info_list_logic(product_ids)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()


@api_view(['GET'])
def product_info(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_PRODUCT_INFO_API)
    
    data = request.query_params
    product_id = data['id'] if 'id' in data else None
    
    status, response_data, message = product_info_logic(product_id)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
        
@api_view(['POST', 'PATCH'])
def address_operation(request):
    print(constants.BREAKCODE)
    
    status = 'Error'
    response_data = None
    message = "Invalid variables/method"
    data = request.body
    
    if data:
        data = data.decode("utf-8")
        data = json.loads(data)
    
        if request.method == "POST":
            print(constants.INITAITED_ADDRESS_INSERT_API)
                
            status, response_data, message = address_insertion_logic(data)
            
        elif request.method == "PATCH":
            print(constants.INITAITED_ADDRESS_UPDATE_API)
            
            status, response_data, message = address_updation_logic(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def search_functionality(request):
    print(constants.BREAKCODE)
    
    data = request.query_params
    
    status, response_data, message = search_functionality_logic(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['GET'])
def get_state_logic(request):
    print(constants.BREAKCODE)
    
    data = request.query_params
    
    status, response_data, message = get_states(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()


@api_view(['GET'])
def get_district_logic(request):
    print(constants.BREAKCODE)
    
    data = request.query_params
    
    status, response_data, message = get_district(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()
    

@api_view(['GET'])
def get_organizations_logic(request):
    print(constants.BREAKCODE)
    
    data = request.query_params
    
    status, response_data, message = get_organizations(data)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

# @api_view(['POST'])
# def upload_image(request):
#     print(constants.BREAKCODE)
#     print(constants.INITIATED_UPLOAD_IMAGES)
    
#     status, response_data, message = upload_images_logic(request)
    
#     return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()


@api_view(['GET'])
def Category_info(request):
    print(constants.BREAKCODE)
    print(constants.INITAITED_CATEGORY_SEARCH_API)
    
    data = request.query_params
    
    category_id = data.get('category_id')
    
    status, response_data, message = get_category(category_id=category_id)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(['POST'])
def rating_update(request):
    print(constants.BREAKCODE)
    print(constants.UPDATE_RATING)
    
    data = request.body
    if data:
        data = data.decode("utf-8")
        
        data = json.loads(data)
    
    product_id = data.get('product_id')
    rating = data.get('rating')
    
    status, response_data, message = rating_update_logic(product_id=product_id, rating=rating)
    
    return JsendSuccessResponse(status = status,data = response_data, message=message).get_response()

@api_view(["GET"])
def start_stop(request):
    print(constants.BREAKCODE)
    
    status = '0'
    message = "All API's Working Successfully"
    
    return JsendSuccessResponse(status = status, data= None, message=message).get_response()

# @api_view(['GET'])
# def add_data(request):
    
#     data = {"Andhra Pradesh": [
#         "Anantapur",
#         "Chittoor",
#         "East Godavari",
#         "Guntur",
#         "Krishna",
#         "Kurnool",
#         "Nellore",
#         "Prakasam",
#         "Srikakulam",
#         "Visakhapatnam",
#         "Vizianagaram",
#         "West Godavari",
#         "YSR Kadapa"
#     ],
#     "Arunachal Pradesh": [
#         "Tawang",
#         "West Kameng",
#         "East Kameng",
#         "Papum Pare",
#         "Kurung Kumey",
#         "Kra Daadi",
#         "Lower Subansiri",
#         "Upper Subansiri",
#         "West Siang",
#         "East Siang",
#         "Siang",
#         "Upper Siang",
#         "Lower Siang",
#         "Lower Dibang Valley",
#         "Dibang Valley",
#         "Anjaw",
#         "Lohit",
#         "Namsai",
#         "Changlang",
#         "Tirap",
#         "Longding"
#     ],
#     "Assam": [
#         "Baksa",
#         "Barpeta",
#         "Biswanath",
#         "Bongaigaon",
#         "Cachar",
#         "Charaideo",
#         "Chirang",
#         "Darrang",
#         "Dhemaji",
#         "Dhubri",
#         "Dibrugarh",
#         "Goalpara",
#         "Golaghat",
#         "Hailakandi",
#         "Hojai",
#         "Jorhat",
#         "Kamrup Metropolitan",
#         "Kamrup",
#         "Karbi Anglong",
#         "Karimganj",
#         "Kokrajhar",
#         "Lakhimpur",
#         "Majuli",
#         "Morigaon",
#         "Nagaon",
#         "Nalbari",
#         "Dima Hasao",
#         "Sivasagar",
#         "Sonitpur",
#         "South Salmara-Mankachar",
#         "Tinsukia",
#         "Udalguri",
#         "West Karbi Anglong"
#     ],
#     "Bihar": [
#         "Araria",
#         "Arwal",
#         "Aurangabad",
#         "Banka",
#         "Begusarai",
#         "Bhagalpur",
#         "Bhojpur",
#         "Buxar",
#         "Darbhanga",
#         "East Champaran (Motihari)",
#         "Gaya",
#         "Gopalganj",
#         "Jamui",
#         "Jehanabad",
#         "Kaimur (Bhabua)",
#         "Katihar",
#         "Khagaria",
#         "Kishanganj",
#         "Lakhisarai",
#         "Madhepura",
#         "Madhubani",
#         "Munger (Monghyr)",
#         "Muzaffarpur",
#         "Nalanda",
#         "Nawada",
#         "Patna",
#         "Purnia (Purnea)",
#         "Rohtas",
#         "Saharsa",
#         "Samastipur",
#         "Saran",
#         "Sheikhpura",
#         "Sheohar",
#         "Sitamarhi",
#         "Siwan",
#         "Supaul",
#         "Vaishali",
#         "West Champaran"
#     ],
#     "Chandigarh (UT)": ["Chandigarh"],
#     "Chhattisgarh": [
#         "Balod",
#         "Baloda Bazar",
#         "Balrampur",
#         "Bastar",
#         "Bemetara",
#         "Bijapur",
#         "Bilaspur",
#         "Dantewada (South Bastar)",
#         "Dhamtari",
#         "Durg",
#         "Gariyaband",
#         "Janjgir-Champa",
#         "Jashpur",
#         "Kabirdham (Kawardha)",
#         "Kanker (North Bastar)",
#         "Kondagaon",
#         "Korba",
#         "Korea (Koriya)",
#         "Mahasamund",
#         "Mungeli",
#         "Narayanpur",
#         "Raigarh",
#         "Raipur",
#         "Rajnandgaon",
#         "Sukma",
#         "Surajpur",
#         "Surguja"
#     ],
#     "Dadra and Nagar Haveli (UT)": ["Dadra & Nagar Haveli"],
#     "Daman and Diu (UT)": ["Daman", "Diu"],
#     "Delhi (NCT)": [
#         "Central Delhi",
#         "East Delhi",
#         "New Delhi",
#         "North Delhi",
#         "North East Delhi",
#         "North West Delhi",
#         "Shahdara",
#         "South Delhi",
#         "South East Delhi",
#         "South West Delhi",
#         "West Delhi"
#     ],
#     "Goa": ["North Goa", "South Goa"],
#     "Gujarat": [
#         "Ahmedabad",
#         "Amreli",
#         "Anand",
#         "Aravalli",
#         "Banaskantha (Palanpur)",
#         "Bharuch",
#         "Bhavnagar",
#         "Botad",
#         "Chhota Udepur",
#         "Dahod",
#         "Dangs (Ahwa)",
#         "Devbhoomi Dwarka",
#         "Gandhinagar",
#         "Gir Somnath",
#         "Jamnagar",
#         "Junagadh",
#         "Kachchh",
#         "Kheda (Nadiad)",
#         "Mahisagar",
#         "Mehsana",
#         "Morbi",
#         "Narmada (Rajpipla)",
#         "Navsari",
#         "Panchmahal (Godhra)",
#         "Patan",
#         "Porbandar",
#         "Rajkot",
#         "Sabarkantha (Himmatnagar)",
#         "Surat",
#         "Surendranagar",
#         "Tapi (Vyara)",
#         "Vadodara",
#         "Valsad"
#     ],
#     "Haryana": [
#         "Ambala",
#         "Bhiwani",
#         "Charkhi Dadri",
#         "Faridabad",
#         "Fatehabad",
#         "Gurgaon",
#         "Hisar",
#         "Jhajjar",
#         "Jind",
#         "Kaithal",
#         "Karnal",
#         "Kurukshetra",
#         "Mahendragarh",
#         "Mewat",
#         "Palwal",
#         "Panchkula",
#         "Panipat",
#         "Rewari",
#         "Rohtak",
#         "Sirsa",
#         "Sonipat",
#         "Yamunanagar"
#     ],
#     "Himachal Pradesh": [
#         "Bilaspur",
#         "Chamba",
#         "Hamirpur",
#         "Kangra",
#         "Kinnaur",
#         "Kullu",
#         "Lahaul & Spiti",
#         "Mandi",
#         "Shimla",
#         "Sirmaur (Sirmour)",
#         "Solan",
#         "Una"
#     ],
#     "Jammu and Kashmir": [
#         "Anantnag",
#         "Bandipore",
#         "Baramulla",
#         "Budgam",
#         "Doda",
#         "Ganderbal",
#         "Jammu",
#         "Kargil",
#         "Kathua",
#         "Kishtwar",
#         "Kulgam",
#         "Kupwara",
#         "Leh",
#         "Poonch",
#         "Pulwama",
#         "Rajouri",
#         "Ramban",
#         "Reasi",
#         "Samba",
#         "Shopian",
#         "Srinagar",
#         "Udhampur"
#     ],
#     "Jharkhand": [
#         "Bokaro",
#         "Chatra",
#         "Deoghar",
#         "Dhanbad",
#         "Dumka",
#         "East Singhbhum",
#         "Garhwa",
#         "Giridih",
#         "Godda",
#         "Gumla",
#         "Hazaribag",
#         "Jamtara",
#         "Khunti",
#         "Koderma",
#         "Latehar",
#         "Lohardaga",
#         "Pakur",
#         "Palamu",
#         "Ramgarh",
#         "Ranchi",
#         "Sahibganj",
#         "Seraikela-Kharsawan",
#         "Simdega",
#         "West Singhbhum"
#     ],
#     "Karnataka": [
#         "Bagalkot",
#         "Ballari (Bellary)",
#         "Belagavi (Belgaum)",
#         "Bengaluru (Bangalore) Rural",
#         "Bengaluru (Bangalore) Urban",
#         "Bidar",
#         "Chamarajanagar",
#         "Chikballapur",
#         "Chikkamagaluru (Chikmagalur)",
#         "Chitradurga",
#         "Dakshina Kannada",
#         "Davangere",
#         "Dharwad",
#         "Gadag",
#         "Hassan",
#         "Haveri",
#         "Kalaburagi (Gulbarga)",
#         "Kodagu",
#         "Kolar",
#         "Koppal",
#         "Mandya",
#         "Mysuru (Mysore)",
#         "Raichur",
#         "Ramanagara",
#         "Shivamogga (Shimoga)",
#         "Tumakuru (Tumkur)",
#         "Udupi",
#         "Uttara Kannada (Karwar)",
#         "Vijayapura (Bijapur)",
#         "Yadgir"
#     ],
#     "Kerala": [
#         "Alappuzha",
#         "Ernakulam",
#         "Idukki",
#         "Kannur",
#         "Kasaragod",
#         "Kollam",
#         "Kottayam",
#         "Kozhikode",
#         "Malappuram",
#         "Palakkad",
#         "Pathanamthitta",
#         "Thiruvananthapuram",
#         "Thrissur",
#         "Wayanad"
#     ],
#     "Lakshadweep (UT)": [
#         "Agatti",
#         "Amini",
#         "Androth",
#         "Bithra",
#         "Chethlath",
#         "Kavaratti",
#         "Kadmath",
#         "Kalpeni",
#         "Kilthan",
#         "Minicoy"
#     ],
#     "Madhya Pradesh": [
#         "Agar Malwa",
#         "Alirajpur",
#         "Anuppur",
#         "Ashoknagar",
#         "Balaghat",
#         "Barwani",
#         "Betul",
#         "Bhind",
#         "Bhopal",
#         "Burhanpur",
#         "Chhatarpur",
#         "Chhindwara",
#         "Damoh",
#         "Datia",
#         "Dewas",
#         "Dhar",
#         "Dindori",
#         "Guna",
#         "Gwalior",
#         "Harda",
#         "Hoshangabad",
#         "Indore",
#         "Jabalpur",
#         "Jhabua",
#         "Katni",
#         "Khandwa",
#         "Khargone",
#         "Mandla",
#         "Mandsaur",
#         "Morena",
#         "Narsinghpur",
#         "Neemuch",
#         "Panna",
#         "Raisen",
#         "Rajgarh",
#         "Ratlam",
#         "Rewa",
#         "Sagar",
#         "Satna",
#         "Sehore",
#         "Seoni",
#         "Shahdol",
#         "Shajapur",
#         "Sheopur",
#         "Shivpuri",
#         "Sidhi",
#         "Singrauli",
#         "Tikamgarh",
#         "Ujjain",
#         "Umaria",
#         "Vidisha"
#     ],
#     "Maharashtra": [
#         "Ahmednagar",
#         "Akola",
#         "Amravati",
#         "Aurangabad",
#         "Beed",
#         "Bhandara",
#         "Buldhana",
#         "Chandrapur",
#         "Dhule",
#         "Gadchiroli",
#         "Gondia",
#         "Hingoli",
#         "Jalgaon",
#         "Jalna",
#         "Kolhapur",
#         "Latur",
#         "Mumbai City",
#         "Mumbai Suburban",
#         "Nagpur",
#         "Nanded",
#         "Nandurbar",
#         "Nashik",
#         "Osmanabad",
#         "Palghar",
#         "Parbhani",
#         "Pune",
#         "Raigad",
#         "Ratnagiri",
#         "Sangli",
#         "Satara",
#         "Sindhudurg",
#         "Solapur",
#         "Thane",
#         "Wardha",
#         "Washim",
#         "Yavatmal"
#     ],
#     "Manipur": [
#         "Bishnupur",
#         "Chandel",
#         "Churachandpur",
#         "Imphal East",
#         "Imphal West",
#         "Jiribam",
#         "Kakching",
#         "Kamjong",
#         "Kangpokpi",
#         "Noney",
#         "Pherzawl",
#         "Senapati",
#         "Tamenglong",
#         "Tengnoupal",
#         "Thoubal",
#         "Ukhrul"
#     ],
#     "Meghalaya": [
#         "East Garo Hills",
#         "East Jaintia Hills",
#         "East Khasi Hills",
#         "North Garo Hills",
#         "Ri Bhoi",
#         "South Garo Hills",
#         "South West Garo Hills",
#         "South West Khasi Hills",
#         "West Garo Hills",
#         "West Jaintia Hills",
#         "West Khasi Hills"
#     ],
#     "Mizoram": [
#         "Aizawl",
#         "Champhai",
#         "Kolasib",
#         "Lawngtlai",
#         "Lunglei",
#         "Mamit",
#         "Saiha",
#         "Serchhip"
#     ],
#     "Nagaland": [
#         "Dimapur",
#         "Kiphire",
#         "Kohima",
#         "Longleng",
#         "Mokokchung",
#         "Mon",
#         "Peren",
#         "Phek",
#         "Tuensang",
#         "Wokha",
#         "Zunheboto"
#     ],
#     "Odisha": [
#         "Angul",
#         "Balangir",
#         "Balasore (Baleswar)",
#         "Bargarh (Baragarh)",
#         "Bhadrak",
#         "Boudh (Bauda)",
#         "Cuttack",
#         "Deogarh (Debagarh)",
#         "Dhenkanal",
#         "Gajapati",
#         "Ganjam",
#         "Jagatsinghpur",
#         "Jajpur",
#         "Jharsuguda",
#         "Kalahandi",
#         "Kandhamal",
#         "Kendrapara",
#         "Kendujhar (Keonjhar)",
#         "Khordha",
#         "Koraput",
#         "Malkangiri",
#         "Mayurbhanj",
#         "Nabarangpur",
#         "Nayagarh",
#         "Nuapada",
#         "Puri",
#         "Rayagada",
#         "Sambalpur",
#         "Sonepur",
#         "Sundargarh"
#     ],
#     "Puducherry (UT)": ["Karaikal", "Mahe", "Puducherry", "Yanam"],
#     "Punjab": [
#         "Amritsar",
#         "Barnala",
#         "Bathinda",
#         "Faridkot",
#         "Fatehgarh Sahib",
#         "Fazilka",
#         "Ferozepur",
#         "Gurdaspur",
#         "Hoshiarpur",
#         "Jalandhar",
#         "Kapurthala",
#         "Ludhiana",
#         "Mansa",
#         "Moga",
#         "Muktsar",
#         "Nawanshahr (Shahid Bhagat Singh Nagar)",
#         "Pathankot",
#         "Patiala",
#         "Rupnagar",
#         "Sahibzada Ajit Singh Nagar (Mohali)",
#         "Sangrur",
#         "Tarn Taran"
#     ],
#     "Rajasthan": [
#         "Ajmer",
#         "Alwar",
#         "Banswara",
#         "Baran",
#         "Barmer",
#         "Bharatpur",
#         "Bhilwara",
#         "Bikaner",
#         "Bundi",
#         "Chittorgarh",
#         "Churu",
#         "Dausa",
#         "Dholpur",
#         "Dungarpur",
#         "Hanumangarh",
#         "Jaipur",
#         "Jaisalmer",
#         "Jalore",
#         "Jhalawar",
#         "Jhunjhunu",
#         "Jodhpur",
#         "Karauli",
#         "Kota",
#         "Nagaur",
#         "Pali",
#         "Pratapgarh",
#         "Rajsamand",
#         "Sawai Madhopur",
#         "Sikar",
#         "Sirohi",
#         "Sri Ganganagar",
#         "Tonk",
#         "Udaipur"
#     ],
#     "Sikkim": ["East Sikkim", "North Sikkim", "South Sikkim", "West Sikkim"],
#     "Tamil Nadu": [
#         "Ariyalur",
#         "Chennai",
#         "Coimbatore",
#         "Cuddalore",
#         "Dharmapuri",
#         "Dindigul",
#         "Erode",
#         "Kanchipuram",
#         "Kanyakumari",
#         "Karur",
#         "Krishnagiri",
#         "Madurai",
#         "Nagapattinam",
#         "Namakkal",
#         "Nilgiris",
#         "Perambalur",
#         "Pudukkottai",
#         "Ramanathapuram",
#         "Salem",
#         "Sivaganga",
#         "Thanjavur",
#         "Theni",
#         "Thoothukudi (Tuticorin)",
#         "Tiruchirappalli",
#         "Tirunelveli",
#         "Tiruppur",
#         "Tiruvallur",
#         "Tiruvannamalai",
#         "Tiruvarur",
#         "Vellore",
#         "Viluppuram",
#         "Virudhunagar"
#     ],
#     "Telangana": [
#         "Adilabad",
#         "Bhadradri Kothagudem",
#         "Hyderabad",
#         "Jagtial",
#         "Jangaon",
#         "Jayashankar Bhoopalpally",
#         "Jogulamba Gadwal",
#         "Kamareddy",
#         "Karimnagar",
#         "Khammam",
#         "Kumuram Bheem Asifabad",
#         "Mahabubabad",
#         "Mahabubnagar",
#         "Mancherial",
#         "Medak",
#         "Medchal-Malkajgiri",
#         "Mulugu",
#         "Nagarkurnool",
#         "Nalgonda",
#         "Narayanpet",
#         "Nirmal",
#         "Nizamabad",
#         "Peddapalli",
#         "Rajanna Sircilla",
#         "Rangareddy",
#         "Sangareddy",
#         "Siddipet",
#         "Suryapet",
#         "Vikarabad",
#         "Wanaparthy",
#         "Warangal (Rural)",
#         "Warangal (Urban)",
#         "Yadadri Bhuvanagiri"
#     ],
#     "Tripura": [
#         "Dhalai",
#         "Gomati",
#         "Khowai",
#         "North Tripura",
#         "Sepahijala",
#         "South Tripura",
#         "Unakoti",
#         "West Tripura"
#     ],
#     "Uttar Pradesh": [
#         "Agra",
#         "Aligarh",
#         "Ambedkar Nagar",
#         "Amethi (Chatrapati Sahuji Mahraj Nagar)",
#         "Amroha (J.P. Nagar)",
#         "Auraiya",
#         "Azamgarh",
#         "Baghpat",
#         "Bahraich",
#         "Ballia",
#         "Balrampur",
#         "Banda",
#         "Barabanki",
#         "Bareilly",
#         "Basti",
#         "Bhadohi",
#         "Bijnor",
#         "Budaun",
#         "Bulandshahr",
#         "Chandauli",
#         "Chitrakoot",
#         "Deoria",
#         "Etah",
#         "Etawah",
#         "Faizabad",
#         "Farrukhabad",
#         "Fatehpur",
#         "Firozabad",
#         "Gautam Buddha Nagar",
#         "Ghaziabad",
#         "Ghazipur",
#         "Gonda",
#         "Gorakhpur",
#         "Hamirpur",
#         "Hapur (Panchsheel Nagar)",
#         "Hardoi",
#         "Hathras",
#         "Jalaun",
#         "Jaunpur",
#         "Jhansi",
#         "Kannauj",
#         "Kanpur Dehat",
#         "Kanpur Nagar",
#         "Kasganj (Kanshiram Nagar)",
#         "Kaushambi",
#         "Kushinagar (Padrauna)",
#         "Lakhimpur - Kheri",
#         "Lalitpur",
#         "Lucknow",
#         "Maharajganj",
#         "Mahoba",
#         "Mainpuri",
#         "Mathura",
#         "Mau",
#         "Meerut",
#         "Mirzapur",
#         "Moradabad",
#         "Muzaffarnagar",
#         "Pilibhit",
#         "Pratapgarh",
#         "Raebareli",
#         "Rampur",
#         "Saharanpur",
#         "Sambhal (Bhim Nagar)",
#         "Sant Kabir Nagar",
#         "Shahjahanpur",
#         "Shamali (Prabuddh Nagar)",
#         "Shravasti",
#         "Siddharth Nagar",
#         "Sitapur",
#         "Sonbhadra",
#         "Sultanpur",
#         "Unnao",
#         "Varanasi"
#     ],
#     "Uttarakhand": [
#         "Almora",
#         "Bageshwar",
#         "Chamoli",
#         "Champawat",
#         "Dehradun",
#         "Haridwar",
#         "Nainital",
#         "Pauri Garhwal",
#         "Pithoragarh",
#         "Rudraprayag",
#         "Tehri Garhwal",
#         "Udham Singh Nagar",
#         "Uttarkashi"
#     ],
#     "West Bengal": [
#         "Alipurduar",
#         "Bankura",
#         "Birbhum",
#         "Burdwan (Bardhaman)",
#         "Cooch Behar",
#         "Dakshin Dinajpur (South Dinajpur)",
#         "Darjeeling",
#         "Hooghly",
#         "Howrah",
#         "Jalpaiguri",
#         "Jhargram",
#         "Kalimpong",
#         "Kolkata",
#         "Malda",
#         "Murshidabad",
#         "Nadia",
#         "North 24 Parganas",
#         "Paschim Medinipur (West Medinipur)",
#         "Purba Medinipur (East Medinipur)",
#         "Purulia",
#         "South 24 Parganas",
#         "Uttar Dinajpur (North Dinajpur)"
#     ]}
    
    
#     for key, values in data.items():
#         print("=====================================================================================")
#         print(f"Adding state {key}")
#         state_name = key
        
#         new_state = TblState.objects.create(state_name = state_name)
        
#         print(f"Added state {key} as {new_state.id}")
        
#         for value in values:
#             print("***********************************************************************************")
#             print("***********************************************************************************")
#             print(f"Adding district {value} in state {state_name}")
            
#             new_district = TblDistrict.objects.create(district_name = value, state = new_state)
            
#             print(f"Added new district  {new_district} as {new_district.id}")
#             print("***********************************************************************************")
            
#         print("=====================================================================================")

#     return JsendSuccessResponse(status = True,data = {}, message="Done").get_response()

