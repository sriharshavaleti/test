import xlrd
import json
import boto3
import numpy as np
import pandas as pd
import urllib.request

def test():
    try:
        dls = "https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls" 
        urllib.request.urlretrive(dls, "test.xls")  # Downloading the xls and storing in local path
        df = pd.read_excel("test.xls", sheetname="MICs List by CC") # Reading the sheetname
        columns = df.columns.values.tolist()
        data = np.array(df)
        num_rows, num_cols = data.shape
        json_list = []
        columns_list = []
        count = 1
        for i in num_rows:
            for j in num_cols:
                columns_dict = {columns[j]: data[count][j]}
                columns_list.append(columns_dict)
            count += 1
            output_dict = {columns_list}
            json_list.append(output_dict)
        data = {json_list}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)	
        s3 = boto3.resource('s3')
        s3.create_bucket(Bucket='jsonbucket')
        s3.Object('jsonbucket', 'data.json').put(Body=open('data.json', 'rb'))
    except (BaseException, ImportError, AssertionError, ValueError, KeyError) as error:
        print('An exception occurred: {}'.format(error))
