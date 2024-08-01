#!/bin/bash

# Activate virtual environment
source /home/pato-devops/VueProjects/tevinswebapp/webbackend/webbackendvenv/bin/activate

# Django command to run shell
python manage.py shell <<EOF

# Import necessary models
from product.models import Product
from brands.models import Brand
from uuid import UUID

try:
    # Replace 'YOUR_BRAND_ID' with the actual UUID causing the issue
    brand_id = UUID('3cdcec8f-b694-46e4-a331-3e19cf431ef9')

    # Retrieve the Brand object
    brand = Brand.objects.get(id=brand_id)
    
    # Example of updating a Product instance
    try:
        product = Product.objects.get(title='Yule')
        product.brand = brand
        product.save()
        print("Product updated successfully with brand:", brand.title)
    except Product.DoesNotExist:
        print("Product with title='Yule' does not exist.")
    except Exception as e:
        print("Error updating product:", str(e))

except Brand.DoesNotExist:
    # Handle the case where the Brand with the given 'brand_id' doesn't exist
    print("Brand with id={} does not exist.".format(brand_id))
except Exception as e:
    # Handle any other exceptions, such as database errors
    print("Error:", str(e))

EOF

# Deactivate virtual environment
deactivate

