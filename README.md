## Pitch Perfect


## Author
Pauline Wafula

## Description
Pitch Perfect is a web application that allows a user to create a one minute pitch depending on the category of interest. a list of various news categories and sources. On clicking a news source, it will give you various choices. Clicking categories, it will give you various categories from health to sports etc. It achieves this by using the [News API](https://newsapi.org/).


## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See the headlines
* Select the source of preference from CNN to ALJAZEERA
* See the top news articles from the source
* See the image,title, description and time the news article was created
* click go to article button to read more about the news

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display headlines  | **On page load** | List of various categories from health to sport with their title, description and time it was published |
| Display tabs with news by category and sources | **On Tab Dropdownlink click** | Clickable links to open news based on category and sources |
| Display articles from a  source | **Click a news source** | Redirected to a page with articles from the source |
| Display the articles of a category | **On page load** | Each article displays an image,description and publication date of the specified category|
| To Read an entire article  | **Click a go to article button** | Redirected to the  source's site to read the entire article |


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* activate virtual environment

### Cloning
* In your terminal:

        $ git clone https://github.com/paulinenanzala19/News_API.git
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

* Setting up the API Key

        To be able to gather article info from the News API you will need an API Key.

        * Visit https://newsapi.org/ and register to generate an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it:

                export NEWS_API_KEY='<Your-Api-Key>'
                export SECRET_KEY='<Your-secret-key>
                python3.8 manage.py server

        * Replace <Your-Api-Key> with your api key and <Your-secret-key> with your secret key

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py tests

## Technologies Used
* Python3.8
* Flask
* HTML
* CSS(Bootstrap)

## live link
['https://nanzalahub.herokuapp.com/']

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