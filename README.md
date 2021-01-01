# dataprep-explorer

A simple Web application to explore [Google Cloud Storage](https://cloud.google.com/storage) files with [Google Cloud Dataprep by Trifacta](https://cloud.google.com/dataprep).

 ![alt tag](https://github.com/victorcouste/dataprep-explorer/blob/master/static/dataprep_explorer.png)

This application creates all the necessary Dataprep objects (Dataset, Flow and Recipe) and generate URLs to the Dataprep interfaces.

This Web application use Python Flask Web framework and Dataprep REST API (https://api.trifacta.com/).

Python source code using Dataprep API can be found in [create_dataprep_objects.py](https://github.com/victorcouste/dataprep-explorer/blob/master/create_dataprep_objects.py) file.

## Installation

* Clone this repo

      git clone https://github.com/victorcouste/dataprep-explorer.git
      
* Install the requirements (in a virtual environment)

      pip install -r requirements.txt

If need more details on Flask framework installation and configuration, [see here](https://flask.palletsprojects.com/en/1.1.x/installation/)

## Running

1/ Update 2 parameters in [create_dataprep_objects.py](https://github.com/victorcouste/dataprep-explorer/blob/master/create_dataprep_objects.py) Python file:

* DATAPREP_AUTH_TOKEN  : The token to use API and to authenticate to Dataprep, it can be generated from Dataprep UI with a project's owner user
* DATAPREP_FOLDERID : The Dataprep folder flow ID where you want to generate flows

2/ Start the Flask Web app

In the Dataprep Explorer directory run:
```shell script
FLASK_APP=datataprep-explorer.py
flask run --port 5000
```
  
Now you must be able to go to http://127.0.0.1:5000/ and play with the application:
  
  ![alt tag](https://github.com/victorcouste/dataprep-explorer/blob/master/Explore_a_Google_GCS_file_with_Cloud_Dataprep.png)
