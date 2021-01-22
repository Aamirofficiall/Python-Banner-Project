# Problem
It was a Banner design for which I have to build api's and Admin Forms.

## Proposed Solution?
According to design the those fields  which could be at most 1 e.g. title,description these types of fields are kept 
indvisual and those fileds which could be more than 1 e.g. (hotel[titel,image,redirect_url]) are kept dynamic by creating separte models.

User can access and create a whole banner including (hotel info and category info) through a single call ,or user can also create Banner, Hotel, categories models indivsually.

## DataBase Models

### Banner:
This model present the whole structure of Banner which includes all neccessarry data of three tabs.It includes those fields which will be same for everytime for any Banner.
  1. title
  2. detail_title
  3. conference_date
  4. address
  5. venue
  6. is_featured
  7. city
  8. country
  9. description
  10. registration
  11. travel_info
  12. image



### Hotel:
This model present the Hotel information that represnts slider in the design.
  1. title
  2. image
  3. redirect_url
  3. banner( foreign key of Banner model)

## API's Endpoints
  7. http://127.0.0.1:8000/v1/api/banner/   [GET,POST,LIST,GET,DELETE]

Note:(/v1/api/bannerComplete/) will create a banner object with as much catagories and hotel models as you desire <br/>



## How to run
Follow these procedures

  1. `pip install -r requirments.txt`
  2. `pip manage.py makemigrations`
  3. `pip manage.py migrate`
  4. To Run on LOCALHOST `pip manage.py runserver`

## Tutorial

https://www.loom.com/share/673820bacaab4bb391c4ccc49fe7840b
