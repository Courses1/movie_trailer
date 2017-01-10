
## Movie Trailer  
This is a movie website which shows movie trailers which are prepopulated. 


### Install

`python - version 2.7`

Install dependencies: `pip install -r requirements.txt`

### Running the project
 
 `export FLASK_APP=app.py`
 
 `python -m flask run`

This will start the server on 5000 port and then hit the `localhost:5000` in the browser.

## Project structure
 
 #### API 
 
 Currently there is just one api exposed, which is get for home page. It reads data from `movies.json`.
  
 #### Folder Structure
  
   ```
   ├── data/
   │   ├── movies.json                          # Movies json data
   │── src/                                     
   │   │   ├── controllers                      
   │   │   ├── ├── movie_controller             # Movie controller which is responsible to talk to service layer
   │   │   ├── ├── movie_service                # Service layer which fetches data from file and creates Movie model array 
   │   │   ├── ├── ....
   │   │   ├── models
   │   │   ├── ├── movie                        # Movie model
   │── static                                   # Static imports                 
   │── |   ├── script                           # Javascript files     
   │── |   ├── styles                           # CSS style files 
   │── templates                                # As flask supports jinja templating, using that as template to render movies list            
   │- app.py                                    # From where the execution will begin                           
  ```
   
If there is any issue, do raise it [here](https://github.com/Courses1/movie_trailer/issues).
   
      
      