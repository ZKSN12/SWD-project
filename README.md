# SWD-project
## Motivation and target users
Nowadays, more and more people choose to have a pet as a companion. However, there are circumstances, for example business travels, that pet owners have no time to take care of their pets. Consequently, there is a great demand for pet boarding services. Petty Care was therefore founded aiming to help pet owners find reliable sitters.
The target users of the app are pet owners seeking pet boarding in Indiana and Illinois.


## Functions of Petty Care app
__External Libraries: BootStrap__

URLs and features of the Petty Care web app:

- /petsitterapp/ — Present the home (index) page
- /petsitterapp/sitter/ — List all pet sitters
- etsitterapp/profile/<id>/ — Present the detail information of a pet sitter
- etsitterapp/about/ — Introduce the Pet Care team and services
- etsitterapp/searchresult/ — List pet sitters based on search criterias
- embers/login/ — Log in to a user account
- embers/register/ — Signup the user account 
- embers/logout/ — logout the user account
- embers/yourpage/ — Present the user’s personal info and pets
- bers/addpet/ — Add new pet info
- embers/editpet/<pet_id>/ — Edit an existing pet’s info

### Home (Index) Page
<img src="https://github.com/ZKSN12/SWD-project/blob/main/readme_img/Picture1.png">

- Through the navigation bar, users can access an “about us” page that provides the basic information about the Pet Care team and the services, a “pet sitter” page that shows all the available sitters at Petty Care, and the links to sign up/sign in.
- Users can search pet sitters by zip code and price range. 
    
### Pet Sitters Page
<img src="https://github.com/ZKSN12/SWD-project/blob/main/readme_img/Picture2.png">
    
- The pet sitter page shows some basic information about the sitters and users can click on the sitters’ name to view their profile page.
- The search is also available on pet sitters page as a quick filter.
    
### Pet Sitter’s Profile Page
<img src="https://github.com/ZKSN12/SWD-project/blob/main/readme_img/Picture3.png">
    
- Pet sitter’s profile page shows all detailed information about the pet sitter including the location in google map.
- The user can contact the sitter via the “send email” button. It will generate an email link with a designated recipient.

<img src="https://github.com/ZKSN12/SWD-project/blob/main/readme_img/Picture4.png">

- Logged in users can leave their comments at the sitter’s profile page.
    
### Register Page
<img src="https://github.com/ZKSN12/SWD-project/blob/main/readme_img/Picture5.png">
    
- Users can log in to access their profile page. Guest users can register to experience the full service of Petty Care.

### User Profile Page
<img src="https://github.com/ZKSN12/SWD-project/blob/main/readme_img/Picture6.png">
    
On the user’s profile page, they can add and edit their pet information.
    

## Application Setup Instruction

1. avigate to SWD-project folder
2. ivate the Virtual Environment:
    pipenv shell
3 tall requirements: 
    pip install -r requirements.txt
4. Launch the local server:
    python manage.py runserver
5. Open the Chrome browser, and enter the URL:
http://18.218.104.41:8001/petsitterapp/
6. Login using test credential:
    username: kexin
    password: milkis123

