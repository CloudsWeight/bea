import requests
from dotenv import load_dotenv
import json
import os
load_dotenv()
class BeaData():
    '''
    Basic usage is to create a bd object and make requests to get datasets and parameters.
    The BEA API method is to find your dataset, inspect the list of parameters, 
    find the parameter you like then get the parameter values, then use that to build
    a request to get data from the specific table values you need.
    Here is an example URL to retrieve JSON data from a dataset for all years: 

    'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method=GetData&datasetname=FixedAssets&TableName=FAAt105&year=x&ResultFormat=JSON'

    Basic Data Retrieval syntax examples for BEA API:
        - method = (GetParameterList, GetData, GetParameterValues)
        - dataset = 'FixedAssets'
        - ParameterName = TableName,
        - TableName = FAAt107
        - year = available or 'x' for all
    
    Its up to you to find the specific datasets needed.

    DatasetNames: ( see req_sets())
    NIPA
    NIUnderlyingDetail
    MNE
    FixedAssets
    ITA
    IIP
    InputOutput
    IntlServTrade
    IntlServSTA
    GDPbyIndustry
    Regional
    UnderlyingGDPbyIndustry
    APIDatasetMetaData

    GetParameterList – retrieves a list of the parameters (required and optional) for a particular dataset.
Required Parameters: UserID, Method, DatasetName
Optional Parameters: ResultFormat
https://apps.bea.gov/api/data?&UserID=Your-36Character-Key&method=getparameterlist&datasetname=Regional&ResultFormat=JSON
    
    GetParameterValues – retrieves a list of the valid values for a particular
parameter. Required Parameters: UserID, Method, DatasetName, ParameterName
Optional Parameters: ResultFormat
Result: ParamValue node with attributes that contain the actual permissible values (and usually a description
of the value).
Example Request 1:
https://apps.bea.gov/api/data?&UserID=Your-36CharacterKey&method=GetParameterValues&datasetname=INTLSERVTRADE&ParameterName=Tra
deDirection&ResultFormat=XML

'''
    def __init__(self):
        
        self.bea_key = os.getenv('BEA_Key')
        self.format = 'JSON'
        self.base = f'https://apps.bea.gov/api/data?&UserID={self.bea_key}&method='

    def __str__(self):
        return str(self.get_data())

    def get_datasetlist(self):
        data = []
        resp = json.loads(self.req(self.base+'GETDATASETLIST'))
        dataset = resp["BEAAPI"]["Results"]["Dataset"]
        i, n = 0, len(dataset)
        while i < n:
            data.append(dataset[i]["DatasetName"])
            i += 1
        del data[-1]
        return data
       
    def get_param_list(self, dataset="ITA" ):
        method='GetParameterList'
        params = []
        url = f'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method={method}&datasetname={dataset}&ResultFormat=JSON'
        resp =  json.loads(self.req(url))
        i, n = 0, len(resp["BEAAPI"]["Results"]["Parameter"])
        while i < n:
            if len(resp["BEAAPI"]["Results"]["Parameter"]) > 0:
                params.append(resp["BEAAPI"]["Results"]["Parameter"][i]["ParameterName"])
                i += 1
            else:
                i += 1
                pass
        return params

    def get_param_vals(self, dataset=None, ):
        if dataset != None:
            method='GetParameterValues'
            url = f'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method={method}&datasetname={dataset}&ResultFormat=JSON'
            resp = self.req(url)
            return resp

    def req_dt(self, dataset='FixedAssets', table="FAAt105"):
        method = 'GetData'
        bea_url = f'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method={method}\
&datasetname={dataset}\
&TableName={table}&year=x&ResultFormat=JSON'
# split url for easier typing
        return bea_url #{self.bea_key}&method=GetData&datasetname=FixedAssets&TableName=FAAt105&year=x&ResultFormat=JSON'

# !raw request
    def req(self,url = None): # basic request to any url given
        try:
            if url != None:
                #print(f'\nRequesting URL: {url}\n')
                r = requests.get(url)
                data = json.dumps(r.json(), indent=1)
                return data
            else:
                print('You need to pass an URL')
                pass
        except Exception as e:
            print(f'Encountered an error: {e}')

    def jsonify(self, alot = None):
        if alot != None:
            print(json.dumps(alot, indent=1))

# __ main
def main():
    bd = BeaData()
    alot = bd.get_datasetlist()
    print(alot)
    i, n = 0, len(alot)
    dataset_params = []
    while i < n:
        params = bd.get_param_list(alot[i])
        dataset_params.append({alot[i]:params})
        i += 1
    print(json.dumps(dataset_params, indent=1))
    
    #print(bd.req(bd.url_param_list("UnderlyingGDPbyIndustry")))
    
    #print(bd.req('https://markets.newyorkfed.org//beta/api/ambs/all/results/details/last/1.json'))
    
   
if __name__ == "__main__":
    main()
