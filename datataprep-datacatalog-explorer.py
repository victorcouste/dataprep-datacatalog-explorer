
from flask import Flask, request,render_template,Markup
from datacatalog_functions import get_datacatalog_tables_tags

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    gcp_project="dataprep-premium-demo"
    dataprep_metadata_tag_template="cloud_dataprep_metadata"

    dataprep_flow=""
    dataprep_user=""
    datacatalog_tables_tags=[]

    if request.method == 'POST':
        dataprep_flow=request.form['dataprep_flow']
        dataprep_user=request.form['dataprep_user']
        datacatalog_tables_tags=get_datacatalog_tables_tags(dataprep_flow,dataprep_user,gcp_project,dataprep_metadata_tag_template)

    return render_template('home.html',datacatalog_tables_tags=datacatalog_tables_tags,dataprep_flow=dataprep_flow,dataprep_user=dataprep_user)