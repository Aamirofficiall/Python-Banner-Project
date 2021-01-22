# Problem
It was a Banner design for which I have to build api's and Admin Forms.

## Proposed Solution?
According to design the those fields  which could be at most 1 e.g. title,description these types of fields are kept 
indvisual and those fileds which could be more than 1 e.g. (hotel[titel,image],category[title,'due_date_price','late_price'] etc.) are kept dynamic by creating separte models.

User can access and create a whole banner including (hotel info and category info) through a single call ,or user can also create Banner, Hotel, categories models indivsually.

## DataBase Models

### Banner:
This model present the whole structure of Banner which includes all neccessarry data of three tabs.It includes those fields which will be same for everytime for any Banner.
  1. banner_title
  2. banner_dateOfEvent
  3. banner_address
  4. banner_image
  5. tab1_title
  6. tab1_description
  7. tab2_title
  8. tab2_description
  9. tab3_title
  10. tab3_description
  11. tab3_venue
  12. tab3_address

### Category:
This model present the data  necessary for registration which is shown in a tabular form in design.
  1. category_title
  2. register_price
  3. register_late_price
  4. banner( foreign key of Banner model)

### Hotel:
This model present the Hotel information that represnts slider in the design.
  1. title
  2. image
  3. banner( foreign key of Banner model)

## API's Endpoints
  1. http://127.0.0.1:8000/v1/api/banner/   [LIST,POST]
  2. http://127.0.0.1:8000/v1/api/banner/<int:id>/   [GET,DELETE]
  3. http://127.0.0.1:8000/v1/api/<int:id>/hotel/   [POST]
  4. http://127.0.0.1:8000/v1/api/hotel/   [LIST,GET,DELETE]
  5. http://127.0.0.1:8000/v1/api/<int:id>/category/   [POST]
  6. http://127.0.0.1:8000/v1/api/category/   [LIST,GET,DELETE]
  7. http://127.0.0.1:8000/v1/api/bannerComplete/   [GET,POST,LIST,GET,DELETE]

Note:(/v1/api/bannerComplete/) will create a banner object with as much catagories and hotel models as you desire <br/>



## How to run
Follow these procedures

  1. `pip install -r requirments.txt`
  2. `pip manage.py makemigrations`
  3. `pip manage.py migrate`
  4. To Run on LOCALHOST `pip manage.py runserver`

## Tutorial

https://www.loom.com/share/673820bacaab4bb391c4ccc49fe7840b
