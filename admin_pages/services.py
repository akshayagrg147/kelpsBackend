from .models import TblCategories, TblSubcategories, TblProducts, TblOrganization, TblState, TblDistrict
from health_care.api_serializer import add_products_serializer
import datetime
from login.models import TblUser
import json
from django.db.models import Q
import ast
from dateutil.tz import gettz

# Categories Related Functions
def get_category(user_id = None, category_id = None):
    try:
        if category_id:
            categories = TblCategories.objects.filter(id = category_id).first()
            final_response = {
                        "id"    : categories.id,
                        "name"  : categories.categories_name,
                        "image" : categories.image,
                        "sub_category" : get_sub_category({'user_id' : 15, 'category' : categories.id}, flag = 'internal')
                        }
            
            
        else:
            final_response = []
            if not user_id:
                raise Exception("User is null")
            
            user_obj = TblUser.objects.filter(id = user_id).first()
            if not user_obj:
                raise Exception("User is not present")
            
            categories = TblCategories.objects.all()
        
            for cat_object in categories:
                response = {
                            "id"    : cat_object.id,
                            "name"  : cat_object.categories_name,
                            "image" : cat_object.image
                            }
                
                final_response.append(response)
        
        return True, final_response, "Categories fetched successully"
        
        
    except Exception as e:
        print(f"Error in fetching categories from database as {str(e)}")
        return False, {}, str(e)

def add_category(user_id, data):
    try:
        final_response = []
        message = []
        
        for obj in data:
            category_name = obj.get('name')
            category_image = obj.get('image')
            
            try:
                if category_name:
                    cat_object = TblCategories.objects.filter(categories_name = category_name, created_by = user_id).first()
                    
                    if cat_object:
                        cat_object.categories_name = category_name
                        cat_object.updated_by = user_id
                        cat_object.save()
                        
                        response = {
                            "id"    : cat_object.id,
                            "name"  : cat_object.categories_name,
                            "image" : cat_object.image
                        }
                        
                        final_response.append(response)
                    
                    else:
                        category_object = TblCategories(categories_name = category_name, image = category_image,
                                                        created_by = user_id)
                    
                        category_object.save()
                        
                        cat_object = TblCategories.objects.filter(categories_name = category_name, created_by = user_id).first()
                        
                        response = {
                            "id"    : cat_object.id,
                            "name"  : cat_object.categories_name,
                            "image" : cat_object.image
                        }
                        
                        final_response.append(response)
            
            except Exception as e:
                err_message = f"Error while adding category :- {category_name} as {str(e)}"
                message.append(err_message)
                
        if message:
            return True, final_response, message
        
        else:
            return True, final_response, "Category Added successfully"
                
    except Exception as e:
        print(f"Error in adding category in database as {str(e)}")
        return False, {}, str(e)
    
def update_category(data):
    try:
        category_id = data.get("id")
        
        if not category_id:
            raise Exception("Category id is none")
        
        category_object = TblCategories.objects.filter(id = category_id).first()
        
        if not category_object:
            raise Exception("Category not found")
        
        for key, value in data.items():
            if key == "name":
                category_object.categories_name = value
            if key == "image":
                category_object.image = value
                
            category_object.save()
            
        category_object.updated_by = data.get('user_id')
        category_object.save()
        
        response = {
                    "id"    : category_object.id,
                    "name"  : category_object.categories_name,
                    "image" : category_object.image
                }
        
        return True, response, "Category updated successfully"
        
    except Exception as e:
        print(f"Error in updating category in database as {str(e)}")
        return False, {}, str(e)
    
def delete_category(data):
    try:
        category_id = data.get("id")
        
        if not category_id:
            raise Exception("Category id is none")
        
        global_cat_obj = TblCategories.objects.filter(categories_name = "Global").first()
        
        category_object = TblCategories.objects.filter(id = category_id).first()
        
        if not category_object:
            raise Exception("Category not found")
        
        # sub_categories = TblSubcategories.objects.filter(category=category_id)

        # for sub_obj in sub_categories:
        #     TblProducts.objects.filter(product_sub_category=sub_obj.id).update(product_sub_category=global_sub_obj, product_category = global_cat_obj)
        
        # for sub_cat in sub_categories:
        #     TblOrganization.objects.filter(sub=sub_cat.id).update(sub=global_sub_obj)
        
        TblOrganization.objects.filter(category=category_id).update(category=global_cat_obj)
            
        # Delete subcategories and then the category
        # sub_categories.delete()
        category_object.delete()
                
        return True, {}, "Category deleted successfully"
        
    except Exception as e:
        print(f"Error in deleting category in database as {str(e)}")
        return False, {}, str(e)


# Sub_categories Related Functions
def get_sub_category(data, flag = None):
    try:
        final_response = []
        user_id = data.get('user_id')
        if not user_id:
            raise Exception("User is null")
        
        user_obj = TblUser.objects.filter(id = user_id).first()
        if not user_obj:
            raise Exception("User is not present")
        
        category = data.get('category')
        if category:
            sub_category_obj = TblSubcategories.objects.filter(category = category).all()
        
        else:
            sub_category_obj = TblSubcategories.objects.all()
        
        for sub_obj in sub_category_obj:
            response = {
                        "id"                : sub_obj.id,
                        "name"              : sub_obj.subcategories_name,
                        "image"             : sub_obj.image,
                        "banner_image"      : ast.literal_eval(sub_obj.banner_images),
                        "organization_id"   : sub_obj.category_id,
                        "organization_name" : sub_obj.category.categories_name
                    }
            
            final_response.append(response)
            
        if flag == 'internal':
            return final_response
        return True, final_response, "Sub_category fetched successully"
        
        
    except Exception as e:
        print(f"Error in fetching sub_category from database as {str(e)}")
        if flag == 'internal':
            return {}
        return False, {}, str(e)

def add_sub_category(user_id, data):
    try:
        final_response = []
        message = []
        
        for obj in data:
            parent_category = int(obj.get('category'))
            sub_category_name = obj.get('name')
            sub_category_image = obj.get('image')
            sub_category_banner_image = obj.get('banner_images', "[]")
            
            try:
                if parent_category and sub_category_name and sub_category_image:
                    subcat_object = TblSubcategories.objects.filter(subcategories_name = sub_category_name, created_by = user_id, category = parent_category).first()
                    
                    if subcat_object:
                        subcat_object.subcategories_name = sub_category_name
                        subcat_object.image = sub_category_image
                        subcat_object.banner_images = sub_category_banner_image
                        subcat_object.updated_by = user_id
                        subcat_object.save()
                        
                        response = {
                            "id"                : subcat_object.id,
                            "name"              : subcat_object.subcategories_name,
                            "image"             : subcat_object.image,
                            "banner_images"     : ast.literal_eval(subcat_object.banner_images),
                            "category_id"       : subcat_object.category,
                            "category_name"     : subcat_object.category.categories_name
                        }
                        
                        final_response.append(response)
                    
                    else:
                        organization_object = TblCategories.objects.filter(id = parent_category).first()
                        if organization_object:
                            sub_category_object = TblSubcategories(subcategories_name = sub_category_name,
                                                                category = organization_object,
                                                                image = sub_category_image,
                                                                banner_images = sub_category_banner_image,
                                                                created_by = user_id)
                    
                            sub_category_object.save()
                        
                            subcat_object = TblSubcategories.objects.filter(subcategories_name = sub_category_name, created_by = user_id, category = parent_category).first()
                            
                            response = {
                                "id"                : subcat_object.id,
                                "name"              : subcat_object.subcategories_name,
                                "image"             : subcat_object.image,
                                "banner_image"      : ast.literal_eval(subcat_object.banner_images),
                                "category_id"       : subcat_object.category_id,
                                "category_name"     : subcat_object.category.categories_name
                            }
                            
                            final_response.append(response)
                        
                        else:
                            raise Exception(f"{parent_category} category not found")
            
            except Exception as e:
                err_message = f"Error while adding sub_category :- {sub_category_image} as {str(e)}"
                message.append(err_message)
                
            if message:
                return True, final_response, message
            
            else:
                return True, final_response, "Sub_catogory Added successfully"
                
    except Exception as e:
        print(f"Error in adding Sub_catogory in database as {str(e)}")
        return False, {}, str(e)

def update_sub_category(data):
    try:
        sub_category_id = data.get("id")
        
        if not sub_category_id:
            raise Exception("Category id is none")
        
        subcategory_object = TblSubcategories.objects.filter(id = sub_category_id).first()
        
        if not subcategory_object:
            raise Exception("Category not found")
        
        for key, value in data.items():
            if key == "name":
                subcategory_object.subcategories_name = value
            if key == "image":
                subcategory_object.image = value
            if key == "banner_images":
                subcategory_object.banner_images = str(value)
                
            subcategory_object.save()
            
        subcategory_object.updated_by = data.get('user_id')
        subcategory_object.save()
        
        response = {
                    "id"                : subcategory_object.id,
                    "name"              : subcategory_object.subcategories_name,
                    "image"             : subcategory_object.image,
                    "banner_image"      : ast.literal_eval(subcategory_object.banner_images),
                    "category_id"       : subcategory_object.category_id,
                    "category_name"     : subcategory_object.category.categories_name
                }
        
        return True, response, "sub_category updated successfully"
        
    except Exception as e:
        print(f"Error in updating sub_category in database as {str(e)}")
        return False, {}, str(e)

def delete_sub_category(data):
    try:
        subcat_id = data.get("id")
        
        if not subcat_id:
            raise Exception("sub_category id is none")
        
        global_sub_obj = TblSubcategories.objects.filter(subcategories_name = 'Global').first()
        
        sub_categories = TblSubcategories.objects.filter(id=subcat_id).first()

        if not sub_categories:
            raise Exception("sub_categories not found")
        
        TblProducts.objects.filter(product_sub_category=subcat_id).update(product_sub_category=global_sub_obj)
        TblOrganization.objects.filter(sub=subcat_id).update(sub=global_sub_obj)

        # Delete subcategories and then the category
        sub_categories.delete()
                
        return True, {}, "Sub_category deleted successfully"
        
    except Exception as e:
        print(f"Error in deleting sub_category from database as {str(e)}")
        return False, {}, str(e)


# Organization Related Functions
def get_orgs(data):
    try:
        final_response = []
        user_id = data.get('user_id')
        if not user_id:
            raise Exception("User is null")
        
        user_obj = TblUser.objects.filter(id = user_id).first()
        if not user_obj:
            raise Exception("User is not present")
        
        organization_obj = TblOrganization.objects.all()
        
        for orgs in organization_obj:
            response = {
                        "id"                : orgs.id,
                        "name"              : orgs.org_name,
                        "image"             : orgs.image,
                        "state_id"          : orgs.state.id if orgs.state else '',
                        "state"             : orgs.state.state_name if orgs.state else '',
                        "district_id"       : orgs.district.id if orgs.district else '',
                        "district"          : orgs.district.district_name if orgs.district else '',
                        "category_id"       : orgs.category.id if orgs.category else '',
                        "category_name"     : orgs.category.categories_name if orgs.category else ''
                    }
            
            final_response.append(response)
            
        
        return True, final_response, "Organizations fetched successully"
        
        
    except Exception as e:
        print(f"Error in fetching organizations from database as {str(e)}")
        return False, {}, str(e)

# TODO to add the functionality for state and district if they are not present in db
def add_orgs(data):
    try:
        final_response = []
        message = []
        
        if data:
            for obj in data:
                organization_name = obj.get('name')
                state = obj.get('state')
                district = obj.get('district')
                category = obj.get('category')
                image = obj.get('image')
                
                try:
                    state_obj = None
                    district_obj = None
                    if state:
                        state_obj = TblState.objects.filter(id = state).first()
                    if district:
                        district_obj = TblDistrict.objects.filter(id = district).first()
                    if category:
                        category_obj = TblCategories.objects.filter(id = category).first()
                        
                    organization_obj = TblOrganization(org_name = organization_name,
                                                                    state = state_obj,
                                                                    district = district_obj, category = category_obj, image = image)
                        
                    organization_obj.save()
                    
                    response = {
                        "id"                : organization_obj.id,
                        "name"              : organization_obj.org_name,
                        "image"             : organization_obj.image,
                        "state_id"          : organization_obj.state.id if organization_obj.state else '',
                        "state"             : organization_obj.state.state_name if organization_obj.state else '',
                        "district_id"       : organization_obj.district.id if organization_obj.district else '',
                        "district"          : organization_obj.district.district_name if organization_obj.district else '',
                        "category_id"       : organization_obj.category.id if organization_obj.category else '',
                        "category_name"     : organization_obj.category.categories_name if organization_obj.category else ''
                        # "sub_category_id"   : organization_obj.sub.id if organization_obj.sub else '',
                        # "sub_category_name" : organization_obj.sub.subcategories_name if organization_obj.sub else ''
                    }
                        
                    final_response.append(response)
                
                except Exception as e:
                    err_message = f"Error while adding organization :- {organization_name} as {str(e)}"
                    message.append(err_message)
                    
                if message:
                    return True, final_response, message
                
                else:
                    return True, final_response, "organization Added successfully"
            
        return False, {}, "organization is empty"
                    
    except Exception as e:
        print(f"Error in adding organization in database as {str(e)}")
        return False, {}, str(e)

def update_orgs(data):
    try:
        organization_id = data.get("id")
        
        if not organization_id:
            raise Exception("organization_id id is none")
        
        organization_obj = TblOrganization.objects.filter(id = organization_id).first()
        
        if not organization_obj:
            raise Exception("organization not found")
        
        for key, value in data.items():
            if key == "name":
                organization_obj.org_name = value
            if key == "state":
                if value == -1:
                    organization_obj.state = None
                else:
                    state_obj = TblState.objects.filter(id = value).first()
                    if state_obj:
                        organization_obj.state = state_obj
            if key == 'district':
                if value == -1:
                    organization_obj.district = None
                else:
                    district_obj = TblState.objects.filter(id = value).first()
                    if district_obj:
                        organization_obj.district = district_obj
            if key == "image":
                organization_obj.image = value
            if key == 'sub_id':
                sub_category_object = TblSubcategories.objects.filter(id = value).first()
                if sub_category_object:
                    organization_obj.sub = sub_category_object
            if key == 'category':
                category_object = TblCategories.objects.filter(id = value).first()
                if category_object:
                    organization_obj.category = category_object
                
                
            organization_obj.save()
        
        response = {
                    "id"                : organization_obj.id,
                    "name"              : organization_obj.org_name,
                    "image"             : organization_obj.image,
                    "state_id"          : organization_obj.state.id if organization_obj.state else '',
                    "state"             : organization_obj.state.state_name if organization_obj.state else '',
                    "district_id"       : organization_obj.district.id if organization_obj.district else '',
                    "district"          : organization_obj.district.district_name if organization_obj.district else '',
                    "category_id"       : organization_obj.category.id if organization_obj.category else '',
                    "category_name"     : organization_obj.category.categories_name if organization_obj.category else '',
                    # "sub_category_id"   : organization_obj.sub.id if organization_obj.sub else '',
                    # "sub_category_name" : organization_obj.sub.subcategories_name if organization_obj.sub else ''
                }
        
        return True, response, "Organzation updated successfully"
        
    except Exception as e:
        print(f"Error in updating Organzation in database as {str(e)}")
        return False, {}, str(e)

def delete_orgs(data):
    try:
        org_id = data.get("id")
        
        if not org_id:
            raise Exception("organization id is none")
        
        organization_obj = TblOrganization.objects.filter(id=org_id).first()

        if not organization_obj:
            raise Exception("organization not found")
        
        TblProducts.objects.filter(organization=org_id).update(organization=None)

        # Delete subcategories and then the category
        organization_obj.delete()
                
        return True, {}, "organization deleted successfully"
        
    except Exception as e:
        print(f"Error in deleting organization from database as {str(e)}")
        return False, {}, str(e)



def get_products(data):
    try:
        final_response = []
        user_id = data.get('user_id')
        if not user_id:
            raise Exception("User is null")
        
        user_obj = TblUser.objects.filter(id = user_id).first()
        if not user_obj:
            raise Exception("User is not present")
        
        category = data.get("category")
        sub_category = data.get('sub_category')
        organization = data.get('organization')
        
        query = Q()
        
        if category:
            query &= Q(product_category=category)  # Using icontains for case-insensitive search

        if sub_category:
            query &= Q(product_sub_category=sub_category)

        if organization:
            query &= Q(organization=organization)
        
        if query:
            products_obj = TblProducts.objects.filter(query)
            
        else:
            products_obj = TblProducts.objects.all()
            
        for product_object in products_obj:
            products_images = {}
            images_list = ast.literal_eval(product_object.product_image)
            for i in range(len(images_list)):
                products_images[f"image_{i+1}"] = images_list[i]
            response = {
                        "id"                    : product_object.id,
                        "name"                  : product_object.product_name,
                        "organization_id"       : product_object.product_category_id if product_object.product_category else '',
                        "organization_name"     : product_object.product_category.categories_name if product_object.product_category else '',
                        # "sub_category_id"       : product_object.product_sub_category_id if product_object.product_sub_category else '',
                        # "sub_category_name"     : product_object.product_sub_category.subcategories_name if product_object.product_sub_category else '',
                        "product_organization_id"  : product_object.organization.id if product_object.organization else '',
                        "product_organization"  : product_object.organization.org_name if product_object.organization else '',
                        "price"                 : product_object.price,
                        "description"           : product_object.description,
                        "product_image"         : products_images,
                        "size_available"        : product_object.size_available,
                        "gst_percentage"        : product_object.gst_percentage
                        }
            
            final_response.append(response)
            
        return True, final_response, "Products fetched successully"
        
        
    except Exception as e:
        print(f"Error in fetching products from database as {str(e)}")
        return False, {}, str(e)

def add_products(user_id, data):
    try:
        final_response = []
        message = []
        print(f"Data is add+products is {data}")
        
        for obj in data:
            serializer = add_products_serializer(data=obj)
            serializer.is_valid(raise_exception=True)
            
            product_name            = obj.get('name')
            product_category        = obj.get('category')
            product_sub_category    = obj.get('sub_category')
            product_organization    = obj.get('organization')
            price                   = obj.get('price')
            description             = obj.get('description')
            product_image           = obj.get('image')
            size                    = obj['size'] if 'size' in obj else {}
            state                   = obj.get('state')
            district                = obj.get('district')
            gst_percentage          = obj.get('gst_percentage')
            
            try:
                if state:
                    state = TblState.objects.filter(id = state).first()
                    
                if district:
                    district = TblDistrict.objects.filter(id = district).first()
                    
                product_organization_obj = None
                if product_category:
                    category_object     = TblCategories.objects.filter(id=product_category).first()
                    if not category_object:
                        raise Exception(f"category not available as id {product_category}")
                
                
                if not product_category:
                    category_object = TblCategories.objects.filter(categories_name = "Global").first()
                    product_category = category_object.id
                    
                # if not product_sub_category:
                #     sub_category_object = TblSubcategories.objects.filter(subcategories_name = "Global").first()
                #     product_sub_category = sub_category_object.id
                    
                if product_organization:
                    product_organization_obj = TblOrganization.objects.filter(id = product_organization).first()
                    if not product_organization_obj:
                        raise Exception(f"Organization not available as id {product_organization}")

                    state = product_organization_obj.state if not state else state
                    
                    district = product_organization_obj.district if not district else district
                
                query = Q()
                if product_name:
                    query &= Q(product_name = product_name)
                
                if product_category:
                    query &= Q(product_category=product_category)  # Using icontains for case-insensitive search

                if product_sub_category:
                    query &= Q(product_sub_category=product_sub_category)

                if product_organization:
                    query &= Q(organization=product_organization)
                    
                if state:
                    query &= Q(state=state)
                    
                if district:
                    query &= Q(district=district)
                    
                if size:
                    query &= Q(size_available__contains={'size': size})
                
                if price:
                    query &= Q(price=price)
                    
                product_object = TblProducts.objects.filter(query).first()

                product_images = []
                if product_object and product_object.product_image:
                    product_images.extend(ast.literal_eval(product_object.product_image))
                    product_images.extend(product_image)
                    
                else:
                    product_images.extend(product_image)
                
                if product_object:
                    print(f"Product already available as {product_object.id}")
                    # Update existing product
                    product_object.product_name         = product_name if product_name else product_object.product_name
                    product_object.product_category     = category_object
                    # product_object.product_sub_category = sub_category_object
                    product_object.organization         = product_organization_obj if product_organization else product_object.organization
                    product_object.price                = price if price else product_object.price
                    product_object.description          = description if description else product_object.description
                    product_object.product_image        = str(product_images)
                    product_object.size_available       = json.dumps(size) if size else json.dumps(product_object.size_available)
                    product_object.updated_on           = datetime.datetime.now(datetime.timezone.utc)
                    product_object.updated_by           = user_id
                    product_object.gst_percentage       = gst_percentage
                else:
                    # Create new product
                    print(f"Product created")
                    product_object = TblProducts(
                        product_name        = product_name,
                        product_category    = category_object,
                        # product_sub_category= sub_category_object,
                        price               = price,
                        description         = description,
                        product_image       = str(product_images),
                        size_available      = json.dumps(size),
                        created_on          = datetime.datetime.now(datetime.timezone.utc).astimezone(gettz('Asia/Kolkata')),
                        created_by          = user_id,
                        updated_on          = datetime.datetime.now(datetime.timezone.utc).astimezone(gettz('Asia/Kolkata')),
                        updated_by          = user_id,
                        state               = state,
                        district            = district,
                        organization        = product_organization_obj,
                        gst_percentage      = gst_percentage
                    )
                
                product_object.save()
                
                products_images = {}
                images_list = ast.literal_eval(product_object.product_image)
                for i in range(len(images_list)):
                    products_images[f"image_{i+1}"] = images_list[i]
                size_dict = product_object.__dict__['size_available']
                response = {
                        "id"                    : product_object.id,
                        "name"                  : product_object.product_name,
                        "organization_id"       : product_object.product_category_id if product_object.product_category else '',
                        "organization_name"     : product_object.product_category.categories_name if product_object.product_category else '',
                        # "sub_category_id"       : product_object.product_sub_category_id if product_object.product_sub_category else '',
                        # "sub_category_name"     : product_object.product_sub_category.subcategories_name if product_object.product_sub_category else '',
                        "product_organization_id"  : product_object.organization.id if product_object.organization else '',
                        "product_organization"  : product_object.organization.org_name if product_object.organization else '',
                        "price"                 : product_object.price,
                        "description"           : product_object.description,
                        "product_image"         : products_images,
                        "size_available"        : json.loads(size_dict),
                        "gst_percentage"        : product_object.gst_percentage,
                        }
                
                final_response.append(response)
            
            except Exception as e:
                err_message = f"Error while adding product '{product_name}': {str(e)}"
                message.append(err_message)

        if message:
            return True, final_response, message
        else:
            return True, final_response, "Products added successfully"
        
    except Exception as e:
        print(f"Error in adding product to the database: {str(e)}")
        return False, {}, str(e)
     
def update_products(data):
    try:
        product_id = data.get("id")
        
        if not product_id:
            raise Exception("Product id is none")
        
        product_object = TblProducts.objects.filter(id=product_id).first()
        
        if not product_object:
            raise Exception("Product not found")
        
        for key, value in data.items():
            if key == "name":
                product_object.product_name = value
                
            elif key == "image":
                product_images = []
                product_images.extend(value)
                product_object.product_image = str(product_images)
                
            elif key == "price":
                product_object.price = value
                
            elif key == "organization":
                if value == "-1":
                    product_object.organization = None
                else:
                    org_object = TblOrganization.objects.filter(id=value).first()
                    if not org_object:
                        raise Exception("Organization not found")
                    product_object.organization = org_object
                    product_object.state = org_object.state
                    product_object.district = org_object.district
                
            elif key == "sub_category":
                if value == "-1":
                    product_object.product_sub_category = None
                else:
                    sub_cat_object = TblSubcategories.objects.filter(id=value).first()
                    if not sub_cat_object:
                        raise Exception("Sub-category not found")
                    product_object.product_sub_category = sub_cat_object
                
            elif key == "category":
                if value == "-1":
                    product_object.product_category = None
                else:
                    cat_object = TblCategories.objects.filter(id=value).first()
                    if not cat_object:
                        raise Exception("category not found")
                    product_object.product_category = cat_object
                
            elif key == "state":
                if value == -1:
                    product_object.state = None
                else:
                    state_object = TblState.objects.filter(id=value).first()
                    if not state_object:
                        raise Exception("state_object not found")
                    product_object.state = state_object
                
            elif key == "district":
                if value == -1:
                    product_object.district = None
                else:
                    district_object = TblDistrict.objects.filter(id=value).first()
                    if not district_object:
                        raise Exception("district_object not found")
                    product_object.district = district_object
                
            elif key == "description":
                product_object.description = value
                
            elif key == "size":
                product_object.size_available = value  # Ensure value is converted to a JSON string
            elif key == "gst_percentage":
                product_object.gst_percentage = value 
            
        product_object.updated_by = data.get('user_id')
        product_object.size_available = json.dumps(product_object.size_available)
        product_object.save()
        
        products_images = {}
        images_list = ast.literal_eval(product_object.product_image)
        for i in range(len(images_list)):
            products_images[f"image_{i+1}"] = images_list[i]
        
        size_dict = product_object.__dict__['size_available']

        response = {
                    "id"                    : product_object.id,
                    "name"                  : product_object.product_name,
                    "category_id"           : product_object.product_category_id if product_object.product_category else '',
                    "category_name"         : product_object.product_category.categories_name if product_object.product_category else '',
                    # "sub_category_id"       : product_object.product_sub_category_id if product_object.product_sub_category else '',
                    # "sub_category_name"     : product_object.product_sub_category.subcategories_name if product_object.product_sub_category else '',
                    "product_organization_id"  : product_object.organization.id if product_object.organization else '',
                    "product_organization"  : product_object.organization.org_name if product_object.organization else '',
                    "price"                 : product_object.price,
                    "description"           : product_object.description,
                    "product_image"         : products_images,
                    "size_available"        : json.loads(size_dict),
                    "gst_percentage"        : product_object.gst_percentage
                    }
        return True, response, "Product updated successfully"
        
    except Exception as e:
        print(f"Error in updating product in database: {str(e)}")
        return False, {}, str(e)

def delete_product(data):
    try:
        product_id = data.get("id")
        
        if not product_id:
            raise Exception("product_id  is none")
        
        product_obj = TblProducts.objects.filter(id = product_id).first()

        if not product_obj:
            raise Exception("product not found")
        
        product_obj.delete()
                
        return True, {}, "product deleted successfully"
        
    except Exception as e:
        print(f"Error in deleting product from database as {str(e)}")
        return False, {}, str(e)


def product_search_logic(data):
    try:
        final_response = []
        search_id = data['search'].lower() if 'search' in data else None
        
        if not search_id:
            raise Exception("search_id can't be null")
        
        is_id = True
        try:
            search_id = int(search_id)
            is_id = True
        
        except Exception as e:
            is_id = False
            
        if is_id:
            products_obj = TblProducts.objects.filter(id = search_id).all()
        
        else:
            products_obj = TblProducts.objects.filter(product_name__icontains = search_id).all()
            
        if not products_obj:
            raise Exception("Products not found" if not is_id else "Product not found")
        
        for product in products_obj:
            size_dict = product.__dict__['size_available']
            size_dict = json.dumps(size_dict)
            images_list = ast.literal_eval(product.__dict__['product_image'])
            products_images = {}
            for i in range(len(images_list)):
                products_images[f"image_{i+1}"] = images_list[i]
            response = {
                "product_id"            : product.__dict__['id'],
                "product_name"          : product.__dict__['product_name'],
                "product_category_id"   : product.product_category.id if product.product_category else '',
                "product_category"      : product.product_category.categories_name if product.product_category else '',
                # "product_sub_id"        : product.product_sub_category.id if product.product_sub_category else '',
                # "product_sub_category"  : product.product_sub_category.subcategories_name if product.product_sub_category else '',
                "size_available"        : json.loads(size_dict),
                "product_image"         : products_images,
                "price"                 : product.__dict__['price'],
                "gst_percentage"        : product.gst_percentage
            }
            
            if product.__dict__['district_id']:
                response['district_id'] = product.__dict__['district_id']
                response['district_name'] = product.district.district_name
                response['state_id'] = product.district.state_id
                response['state_name'] = product.district.state.state_name
            
            if product.__dict__['state_id']:
                response['state_id'] = product.__dict__['state_id']
                response['state_name'] = product.state.state_name
                
            if product.__dict__['organization_id']:
                response['organization_id'] = product.__dict__['organization_id']
                response['organization_name'] = product.organization.org_name
                response['district_id'] = product.organization.district_id
                response['district_name'] = product.organization.district.district_name if product.organization.district_id else ''
                response['state_id'] = product.organization.state_id
                response['state_name'] = product.organization.state.state_name if product.organization.state else None
            
            final_response.append(response)
            
        return True, final_response, "Product fetch successfull"

    except Exception as e:
        print(f"Error in product_search_logic as  {str(e)}")
        return False, {}, str(e)
 
def organization_search_logic(data):
    try:
        final_response = []
        search_id = data['search'].lower() if 'search' in data else None
        
        if not search_id:
            raise Exception("search_id can't be null")
        
        is_id = True
        try:
            search_id = int(search_id)
            is_id = True
        
        except Exception as e:
            is_id = False
            
        if is_id:
            organization_obj = TblOrganization.objects.filter(id = search_id).all()
        
        else:
            organization_obj = TblOrganization.objects.filter(org_name__icontains = search_id).all()
            
        if not organization_obj:
            raise Exception("Organizations not found" if not is_id else "Organization not found")
        
        for obj in organization_obj:
            final_response.append({
                                    'id'                : obj.id, 
                                    'name'              : obj.org_name, 
                                    'state_id'          : obj.state_id if obj.state else '', 
                                    "state_name"        : obj.state.state_name if obj.state else '', 
                                    'district_id'       : obj.district_id if obj.district else '', 
                                    "district_name"     : obj.district.district_name if obj.district else '' 
                                    # "sub_category_id"   : obj.sub_id if obj.sub else '', 
                                    # "sub_category_name" : obj.sub.subcategories_name if obj.sub else ''
                                    })
                
        return 'Success', final_response, "All organizations found successfully"

    except Exception as e:
        print(f"Error in organization_search_logic as  {str(e)}")
        return False, {}, str(e)
 
def sub_category_search_logic(data):
    try:
        final_response = []
        search_id = data['search'].lower() if 'search' in data else None
        
        if not search_id:
            raise Exception("search_id can't be null")
        
        is_id = True
        try:
            search_id = int(search_id)
            is_id = True
        
        except Exception as e:
            is_id = False
            
        if is_id:
            sub_category_obj = TblSubcategories.objects.filter(id = search_id).all()
        
        else:
            sub_category_obj = TblSubcategories.objects.filter(subcategories_name__icontains = search_id).all()
            
        if not sub_category_obj:
            raise Exception("Sub_categories not found" if not is_id else "Sub_category not found")
        
        for obj in sub_category_obj:
            final_response.append({ 
                                    "id"                    : obj.id,    
                                    "subcategories_name"    : obj.subcategories_name,
                                    "category_id"           : obj.category.id,
                                    "category_name"         : obj.category.categories_name,
                                    "image"                 : obj.image})
                
        return 'Success', final_response, "All Sub_category found successfully"

    except Exception as e:
        print(f"Error in sub_category_search_logic as  {str(e)}")
        return False, {}, str(e)
 
def category_search_logic(data):
    try:
        final_response = []
        search_id = data['search'].lower() if 'search' in data else None
        
        if not search_id:
            raise Exception("search_id can't be null")
        
        is_id = True
        try:
            search_id = int(search_id)
            is_id = True
        
        except Exception as e:
            is_id = False
            
        if is_id:
            category_obj = TblCategories.objects.filter(id = search_id).all()
        
        else:
            category_obj = TblCategories.objects.filter(categories_name__icontains = search_id).all()
            
        if not category_obj:
            raise Exception("Categories not found" if not is_id else "Category not found")
        
        for obj in category_obj:
            final_response.append({ 
                                    "id"                    : obj.id,    
                                    "category_name"         : obj.categories_name,
                                    "image"                 : obj.image,
                                    "state"                 : obj.state if obj.state else ''})
                
        return 'Success', final_response, "All Categories found successfully"

    except Exception as e:
        print(f"Error in category_search_logic as  {str(e)}")
        return False, {}, str(e)
 

 


 


   