from google.cloud import datacatalog
from datetime import datetime

key_path="/Users/victorcoustenoble/Documents/Trifacta/Product/Google/API/Dataprep-Premium-Demo-3758bd87a1ad.json"
datacatalog_client = datacatalog.DataCatalogClient.from_service_account_json(key_path)

def get_datacatalog_tables_tags(flow,user,project, dataprep_tag_template):

	datacatalog_tables_tags=[]

	tables = get_dataprep_tables(flow,user,project,dataprep_tag_template)

	for table in tables:

		tag=get_tags_table(table.relative_resource_name,dataprep_tag_template)

		dataprep_job_timestamp=tag.fields['dataprep_job_timestamp'].timestamp_value
		job_date = datetime.combine(date=dataprep_job_timestamp.date(), time=dataprep_job_timestamp.time(), tzinfo=dataprep_job_timestamp.tzinfo).strftime("%d/%m/%Y %H:%M")

		table_items=table.linked_resource.split('/')
		table_tag = {
			"table": {
				"relative_resource_name":table.relative_resource_name,
				"dataset":table_items[6],
				"name":table_items[8]
			},
			"tag":tag,
			"job_date":job_date
		}
		#print(table_tag)

		datacatalog_tables_tags.append(table_tag)

	return datacatalog_tables_tags


def get_dataprep_tables(flow,user,project,dataprep_tag_template):

	scope = datacatalog.SearchCatalogRequest.Scope()
	scope.include_project_ids.append(project)

	if flow:
		query='tag:'+dataprep_tag_template+'.dataprep_flow_name:'+flow
	elif user:
		query='tag:'+dataprep_tag_template+'.dataprep_user:'+user
	else:
		query='tag:'+dataprep_tag_template
	
	tables = datacatalog_client.search_catalog(scope=scope, query=query)
	
	return(tables)


def get_tags_table(table_entry_name,dataprep_tag_template):

	for tag in datacatalog_client.list_tags(parent=table_entry_name):

		if dataprep_tag_template in tag.template:
	
			return(tag)

	return None

#datacatalog_tables_tags=get_datacatalog_tables_tags("","","dataprep-premium-demo","cloud_dataprep_metadata")
