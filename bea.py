'''
Very simple requests to retrieve BEA data
'''
#!/usr/bin/env python

import requests
import time

class BEAUrl:
    def __init__(self):
        '''presets'''
        self.key_url = self.set_key()
        self.format = 'JSON'
        self.url = self.build_bea_url()

    def set_key(self, key = '#PERSONAL_BEA_KEY'):
        '''set API key'''
        self.key = key
        key_url = f"&UserID={self.key}"
        return key_url

    def get_datasets(self):
        '''store datasets url piece'''
        get_data_set_url = f"&method=GetDataSetList"

    def build_bea_url(self):
        '''build up an url for a request'''
        root_url = f"https://apps.bea.gov/api/data?"
        method_url =f"method=GetParameterValues"
        data_set_name = f"&datasetname=INTLSERVTRADE"
        parameter_name =f"&ParameterName= TradeDirection"
        built_url = root_url+self.key_url+method_url+data_set_name+parameter_name+self.format
        # method=getparameterlist&datasetname=Regional&ResultFormat=JSON
        return built_url

    def get_bea_datasets(self):
        '''return the bea datasets available'''
        r = requests.get(self.url)
        return r.json()


def main():
    bea1 = BEAURL()
    print(bea1.url)
    bea1.get_bea_datasets()
if __name__ == "__main__":
    main()

'''                 DOCS AND NOTES

******** Response for 'url' of currently offered datasets: ******
        'GETDATASETLIST'}]}, 'Results':
        {'Dataset': [
        {'DatasetName': 'NIPA', 'DatasetDescription': 'Standard NIPA tables'}, {'DatasetName': 'NIUnderlyingDetail', 'DatasetDescription': 'Standard NI underlying detail tables'},
        {'DatasetName': 'MNE', 'DatasetDescription': 'Multinational Enterprises'},
        {'DatasetName': 'FixedAssets', 'DatasetDescription': 'Standard Fixed Assets tables'},
        {'DatasetName': 'ITA', 'DatasetDescription': 'International Transactions Accounts'},
        {'DatasetName': 'IIP', 'DatasetDescription': 'International Investment Position'},
        {'DatasetName': 'InputOutput', 'DatasetDescription': 'Input-Output Data'},
        {'DatasetName': 'IntlServTrade', 'DatasetDescription': 'International Services Trade'},
        {'DatasetName': 'GDPbyIndustry', 'DatasetDescription': 'GDP by Industry'},
        {'DatasetName': 'Regional', 'DatasetDescription': 'Regional data sets'},
        {'DatasetName': 'UnderlyingGDPbyIndustry', 'DatasetDescription': 'Underlying GDP by Industry'},
        {'DatasetName': 'APIDatasetMetaData', 'DatasetDescription': 'Metadata about other API datasets'}]}}}


*********************  Request - DOCS  *************************

        Response object = r

        We can get all the information we need from this object, r.

        Requests’ simple API: all forms of HTTP request are obvious.
            ex.) make an HTTP POST request:

            r = requests.post('https://httpbin.org/post', data={'key': 'value'})

         Other HTTP request types: PUT, DELETE,
             HEAD and OPTIONS? These are all just as simple:

            r = requests.put('https://httpbin.org/put', data={'key': 'value'})

            r = requests.delete('https://httpbin.org/delete')

            r = requests.head('https://httpbin.org/get')

            r = requests.options('https://httpbin.org/get')

            builtin JSON decoder, in case you’re dealing with JSON data:

            import requests

            r = requests.get('https://api.github.com/events')

            r.json()

        Use a pattern like this to save what is being streamed to a file:

            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=128):
                    fd.write(chunk)
'''
