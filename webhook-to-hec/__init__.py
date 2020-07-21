import logging
import urllib3

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    #Parse URL Parameters
    request_args = req.params

    http_method = request_args.get('http_method')
    url = request_args.get("url")
    port = request_args.get('port')
    token = request_args.get('token')

    #Build Full URL out of Parameters
    full_url = http_method+'://'+url+':'+port+'/services/collector/raw'
    
    #Get Body
    webhook_body = req.get_body()

    #Create URLLib3 Pool Manager
    http = urllib3.PoolManager()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    #Post Event
    r = http.request('POST', full_url, body=webhook_body, headers={'Content-Type': 'application/json', 'Authorization':'Splunk '+token})
    return func.HttpResponse(
             body="{\"body\": \"Success\",\"statusCode\": 200}",
             status_code=200
    )
