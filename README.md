## Pitch Perfect
You want to pitch that idea out? pitch perfect got you!


## Author
Pauline Wafula

## Description
Pitch Perfect is a web application that allows a user to create a one minute pitch depending on the category of interest.It has four categories; business,idea,pickuplines and  music. On clicking on the click to view button, it displays pitches posted by other people on the same category.A new user can also log in\register to create a quote under category of choice and also comment on other people pitches.A user can also see the pitches posted through their profile.


## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See the categories of pitches displayed as cards
* Select the category of preference from Business to Music
* See pitches posted by other people under category of choice.
* See the uploded profile image,option to edit my bio. 
* click go to pitch to upvote,downvote or comment on the pitches posted. 

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display categories  | **On page load** | List of various categories from business to music with their title and pitch |
| Display page with pitches by category | **On clicking a 'click to view' button** | Clickable links to open pitches on the related category  |
| Display pitches posted by other people | **Click an upvote,downvote or comment** | Redirected to a main page with an increase in one |
| Display the comments from a related pitch | **On clicking comments button** | Displays all|
| Registration/login required  | **** | Redirected to creating a pitch if you already have an account  |


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* activate virtual environment

### Cloning
* In your terminal:

        $ git clone https://github.com/paulinenanzala19/Perfect_Pitches.git
        $ cd News

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.8  pip install flask
        $ python3.8  pip install flask-Bootstrap
        $ python3.8  pip install flask-Script
        $ python3.8  pip install flask-migrate
        $ python3.8  pip install flask-sqlalchemy
        $ python3.8  pip install flask-Reuploded
        $ python3.8  pip install flask-login
        $ python3.8  pip install flask-WTF

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py test

## Technologies Used
* Python3.8
* Flask
* HTML
* CSS(Bootstrap)

## live link
['https://perfectpitches.herokuapp.com/']

## known bugs
Not any at the moment but am open to suggestion


## License
MIT License

Copyright (c) 2022 Pauline Nanzala

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.