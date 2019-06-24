import json
import requests
from requests.auth import HTTPBasicAuth

def lambda_handler(event, context):
    id = event["ID"]
    reference = event["reference"]
    period = event["period"]
    survey = event["survey"]
    output = send(input, id, reference, period, survey)
    return output


def send(input, id, reference, period, survey):
    url = 'https://ons.bpm.ibmcloud.com/baw/dev/teamworks/webservices/BMI2/ReceiveSummary.tws'
    headers = {"content-type": "application/json+xml", "BPMCSRFToken": "<token>"}
    Data= """{
     "reference":" """ + reference + """ ",
     "period":" """ + period + """ ",
     "survey":" """ + survey + """ ",
     "id":" """ + id + """ ",
     "status": "FAIL",
     "exception": [
       {
         "errorDescription": "Desc",
         "phaseRaised": "TAKE ON",
         "errorCode": "01",
         "Step": "Vets",
         "run": "1",
         "anomalies": [
           {
             "question": "Q46",
             "description": "Desc Question",
             "formula": [
             "Formula A"
             ]
           },
           {
             "question": "Q47",
             "description": "Desc Question",
             "formula": [
             "Formula B"
             ]
           },
           {
             "question": "Q48",
             "description": "Desc Question",
             "formula": [
             "Formula D"
             ]
           }
         ]
       }
     ]
   } """
   
    body = """
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:rec="https://ons.bpm.ibmcloud.com/baw/dev/teamworks/webservices/BMI2/ReceiveSummary.tws">
    <soap:Header/>
    <soap:Body>
      <rec:VetsSummary>
        <rec:username><user_name></rec:username>
        <rec:password><password></rec:password>
        <rec:jsonStr>""" + Data.replace('\n','').replace('\t','').replace('     ','') + """</rec:jsonStr>
      </rec:VetsSummary>
    </soap:Body>
    </soap:Envelope>
    """


    response = requests.post(url, data=body, headers=headers, auth=HTTPBasicAuth('<user_name>', '<password>'))
    print(response.content)
