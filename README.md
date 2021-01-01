# Google Cloud Data Catalog Explorer for Dataprep Tags


A simple Web application to explore BigQuery tables tagged in [Google Cloud Data Catalog](https://cloud.google.com/data-catalog/) with [Cloud Dataprep](https://cloud.google.com/dataprep) tags.

 ![alt tag](https://github.com/victorcouste/dataprep-datacatalog-explorer/blob/master/static/dataprep_datacatalog_explorer.png)

This application creates all the necessary Dataprep objects (Dataset, Flow and Recipe) and generate URLs to the Dataprep interfaces.

This Web application use Python Flask Web framework and <a href="https://googleapis.dev/python/datacatalog/latest/index.html#" target="_blank">Python Client for Google Cloud Data Catalog API</a> to search in Data Catalog.

Python source code using Data Catalog API can be found in [datacatalog_functions.py](https://github.com/victorcouste/dataprep-datacatalog-explorer/blob/master/datacatalog_functions.py) file.

## Installation

* Clone this repo

      git clone https://github.com/victorcouste/dataprep-datacatalog-explorer.git
      
* Install the requirements (in a virtual environment)

      pip install -r requirements.txt

If need more details on Flask framework installation and configuration, [see here](https://flask.palletsprojects.com/en/1.1.x/installation/)

## Running

1/ Update the **key_path** parameter in [datacatalog_functions.py](https://github.com/victorcouste/dataprep-datacatalog-explorer/blob/master/datacatalog_functions.py) Python file. This parameter set your <a href="https://googleapis.dev/python/google-api-core/latest/auth.html#service-accounts" target="_blank">service account json key file to authenticating to Google Cloud services</a>.

2/ Start the Flask Web app

In the Dataprep Explorer directory run:
```shell script
FLASK_APP=datataprep-explorer.py
flask run --port 5000
```
  
Now you must be able to go to http://127.0.0.1:5000/ and play with the application:
  
  ![alt tag](https://github.com/victorcouste/dataprep-datacatalog-explorer/blob/master/Search_BigQuery_tables_with_Cloud_Dataprep_Metadata_Tag.png)
