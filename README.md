# **TO RUN THE PROJECT **


## create a vritual environment using virtulenv with following command.
`* python virtualenv v(name of env)*`
##activate the environment with the command 
`* v\Scripts\activate *`
##install all the required modules and framework by the command
`pip install -r requirements.txt`

## go to vendorManagement dir and run following command to configure database and runserver.

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

Go to [localhost]  (http://127.0.0.1:8000/api)
You will see following urls.

admin/
api/ ^vendors/$ [name='vendor-list']
api/ ^vendors\.(?P<format>[name='vendor-list']
api/ ^vendors/(?P<pk> [name='vendor-detail']
api/ ^vendors/(?P<pk>[^/.]+)[name='vendor-detail']
api/ ^purchase-details/$ [name='purchase-list']
api/ ^purchase-details\.(?P<format>[a-z0-9]+)[name='purchase-list']
api/ ^purchase-details/(?P<pk>[^/.]+)/$ [name='purchase-detail']
api/ ^purchase-details/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='purchase-detail']
api/ [name='api-root']


## Example of URLs
### or vendors list go to 
[vendors] (http://127.0.0.1:8000/api/vendors/)
![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/4f23d332-b6b9-457d-83ec-e8d64e0d7742)

### to create new vendor go to editable section or make a post request to same URL mention above.
![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/2c507d26-d00b-41cf-a4d0-0e1982023df4)

### For specific vendor mention vendor id
[vendors/1] http://127.0.0.1:8000/api/vendors/1/
![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/6a41ed9c-54ff-4523-ac07-2373250902d2)

### to update vendor details go to editable section or make a post request to same URL mention above
![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/6670b50a-e4f2-4bba-8ae7-f9dd5f1c9620)

 ## For Purchase order URLs

 ### for purchase order list go to 
 [purchase-details] (http://127.0.0.1:8000/api/purchase-details/)
 ![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/9fcae2c8-1ff7-4c6d-ba3f-4e67848a45e6)

  ## to create new purchase order got to editable order or make a post request with payload to above mention URL
  ![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/c3f48419-3b68-4c0c-9295-3985185980c0)


 ### for specific purchase order mention order id or vendor id
 [purchase-details/1/](http://127.0.0.1:8000/api/purchase-details/1/)

 ![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/5827501c-8278-4895-8c6d-d8b6fbcfcc30)

 ## To update specific Purchase order go to editable section or make a PUT request to above URL with payload
 ![image](https://github.com/LokeshJangid01/Vendor-management-System/assets/67707359/8c21aa8a-b6d2-48ad-a702-c05133c3ca3c)
 




 








