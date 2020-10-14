import requests 
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models

# Create your views here.
#BASE_NUELLIST_URL ='https://losangeles.nuellist.org/search/?query={}'

BASE_NUEL_URL = 'https://bangalore.craigslist.org/search/?query={}'
BASE_IMAGE_URL= 'https://images.craigslist.org/{}_300x300.jpg'    

     

def home(request):
    return render(request ,'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search =search) # add the search to database
    final_url = BASE_NUEL_URL.format(quote_plus(search)) # concatenate whatever typed on the screen and make it a clickable link
    #print(final_url)
    response = requests.get(final_url)
    data = response.text 
    soup =BeautifulSoup(data,features ='html.parser')
    post_title =soup.find_all('a' ,{'class' :'result-title'})

    print(post_title[0])
    print("..................")
    print(post_title[0].text)
    print(len(post_title))
    print(".....entire information......")
    print(post_title[0].get('href'))

    # single div data

    post_listings =soup.find_all('li' ,{"class" :"result-row"})

    #post_title =post_listings[0].find(class_="result-title").text
    #post_url =post_listings[0].find('a').get('href')
    post_price =post_listings[0].find(class_='result-price').text

   

    # fetching all the data in post_listing

    final_postings =[]

    for post in post_listings:

        post_title =post.find(class_="result-title").text
        post_url = post.find('a').get('href')
       

        if post.find(class_="result-price"):
            #post_price =post.find('span').get("result-price")

            post_price =post.find(class_="result-price").text

        else:
            post_price ='N/A' 

        if post.find(class_='result-image').get('data-ids'):
            #post_image = post.find(class_='result-image').get('data-ids').split(',')
     
            #post_image = post.find(class_='result-image').get('data-ids').split(',')[0]
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
           
            print(post_image_id)
            post_image_url = BASE_IMAGE_URL.format(post_image_id) 
            print(post_image_url)  
        else:
            post_image_url ='https://craigslist.org/images/peace.jpg'

        final_postings.append( (post_title, post_url, post_price ,post_image_url) )   

        #   post_price = post.find(class_="result-price").text

        #else:
         #   new_response = requests.get(post_url)
          #  new_data =new_response.text 
           # new_soup = BeautifulSoup(new_data,features="html.parser")
            #post_text =new_soup.find(id="postingbody").text  


    #print("index 0 :" ,final_postings[2])       

    stuff_front_end ={  'search' :search ,'final_postings' :final_postings}

    return render(request ,'my_app/new_search.html' ,stuff_front_end)    










#import requests
#from bs4 import BeautifulSoup
#from django.shortcuts import render
#from requests.compat import quote_plus
#from . import models

#BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
#BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


#def home(request):
 #   return render(request, 'base.html')


#def new_search(request):
 #   search = request.POST.get('search')
  #  models.Search.objects.create(search=search)
   # final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
   # response = requests.get(final_url)
   # data = response.text
    #soup = BeautifulSoup(data, features='html.parser')

    #post_listings = soup.find_all('li', {'class': 'result-row'})

    #final_postings = []

    #for post in post_listings:
     #   post_title = post.find(class_='result-title').text
      #  post_url = post.find('a').get('href')

       # if post.find(class_='result-price'):
        #    post_price = post.find(class_='result-price').text
       # else:
        #    post_price = 'N/A'

        #if post.find(class_='result-image').get('data-ids'):
         #   post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
          #  post_image_url = BASE_IMAGE_URL.format(post_image_id)
           # print(post_image_url)
        #else:
         #   post_image_url = 'https://craigslist.org/images/peace.jpg'

        #final_postings.append((post_title, post_url, post_price, post_image_url))

    #stuff_for_frontend = {
     #   'search': search,
      #  'final_postings': final_postings,
   # }

    #return render(request, 'my_app/new_search.html', stuff_for_frontend)