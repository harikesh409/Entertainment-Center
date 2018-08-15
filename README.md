# Entertainment-Center
A website generator that generates the posters and youtube trailers of your favorite movies.

## Requried Softwares
1. [Python 3](https://www.python.org/downloads/)
2. Any editor to edit the files

## How to use
1. Obtain OMDb API key from [here.](http://www.omdbapi.com/apikey.aspx)
2. Open `entertainment_center.py` file and add the OMBDb API key on line number 9.

      ```
      OMDBapikey = "" # Add your api key in between the quotes
      ```
3. Obtain youtube API key from [here.](https://developers.google.com/youtube/v3/getting-started)
4. In the same file add the youtube key on line number 10.
      ```
      youtubeAPIkey = "" # Add your youtube api key in between the quotes
      ```
5. In the `names` array write your list of favorite movies in an Comma Seperated way.
  For example
      ```
      names = ["forrest gump","Avengers","avatar","inception","fight club","the matrix"]
      ```
6. After editing just save the file.
7. Open Command Prompt/ Terminal and enter the following command to generate the webpage.
      ```
      python entertainment_center.py
      ```
8. Now `index.html` file is generated in the same folder after successful execution of command.

## Python Codes

* `entertainment_center.py`: It contains the main code that calls the APIs and does the instantiations and website build.
* `media.py`: Enables us to create `Movie` objects.
* `fresh_tomatoes.py`: Takes in a list of `Movie` objects, and returns a beautiful HTML webpage with the specified movies.
