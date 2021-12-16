'''
BEA testing

'''
#!/usr/bin/env python

import requests
from key import BEA_Key
import json
class BEAUrl:
    def __init__(self):
        self.bea_key = self.set_key()
        self.format = 'JSON'
        self.params = self.set_bea_params_url()
        self.format = self.set_format()

    def __str__(self):
        return self.params

    def _bea_key(self):
        bea_key = BEA_Key()
        return bea_key.key

    def set_key(self):
        '''set API key'''
        return self._bea_key()

    def set_bea_params_url(self):
         bea_url = f'https://apps.bea.gov/api/data?&UserID={self.bea_key}&method=GETDATASETLIST&{self.format}'
         return bea_url
         '''build up an url for a request'''

    def set_format(self, format = 'JSON'):
        formated = f'&ResultFormat={format}'
        return str(formated)

    def test_get(self):
        url1 = f'https://apps.bea.gov/api/data?&UserID={self.bea_key}&method=GetParameterValues&datasetname=INTLSERVTRADE&ParameterName=TradeDirection&{self.format}'
        url2 = f'https://apps.bea.gov/api/data/?&UserID={self.bea_key}&method=GetData&datasetname=Regional&TableName=CAINC1&LineCode=3&GeoFIPS=CA&Year=2018&{self.format}'
        r = requests.get(url2)
        data = r.json()
        with open('test_data.txt', 'a') as file:
            file.write(json.dumps(data, indent=4))
        return json.dumps(data, indent=4)

    def get_bea_datasets(self):
        '''return the bea datasets available'''
        r = requests.get(self.url)
        data = r.json()

def main():
    bea1 = BEAUrl()
    print(bea1,'\n')
    data = bea1.test_get()
    print(data)
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
