TAGGING MENU ITEMS FROM USER REVIEWS
====================================

Intent:
----------------------------------
    - Two Searches not supported by Food based platforms
        > Best dishes of a restaurant as per customers
        > Best restaurants serving a particular dish

Proposed Solution:
----------------------------------
    - Get food mentions from user reviews for restaurants over Zomato
    - Associate these mentions with menus of respective restaurants

How to Run:
----------------------------------
    1.Navigate to Zomato-Food-Review folder in terminal
    2.Run localhost server using 'php -S localhost:8000'
    3.On browser goto 'localhost:8000/UI/foodie.html', enjoy the platform :)

Data:
----------------------------------
    - Zomato API calls for dailymenu doesn't work, as restaurant menus as images
    - Thus, we manually took menus of few restaurants as image to text was inefficient
    - Also there is a limit of fetching reviews using Zomato API
    - We thus, scraped reviews from zomato site, though we have a Zomato API wrapper

:Codebase Description-

zomato-api-wrapper/:
----------------------------------
	1.zomatoApiModule.py - a python wrapper to the zomato API
	2.driver.py - driver file for zomatoApiModule.py classes

backend/:
----------------------------------
    1.menu_generator.py - Creates restaurant_id to name and menu mappings from menu.csv
    2.readfile.py - Combine Review and Ratings for Individual restaurants
    3.Match.py - Algorithms to match mentions with menu items
    4.POStagger.py [Rule based NER] - Create food mentions from user reviews
    4.Client.py - Creates Search by restaurant and Search by dishes mappings for UI.
    5.data/ - Intermediate data of backend
    6.Ratings/- Ratings by user reviews for restaurants
    7.Reviews/ - Reviews of restaurants
    8.menu.csv -  menu of some restuarants as our dataset

visualize/ [Create Visualization Inferences from  data]:
----------------------------------
    1.visualize_1 - Relate Average Restaurant Price per dish, Words per review length
                    and Restaurant Rating
    2.visualize_2 - Relate Price, Popularity and Ratings of individual dishes