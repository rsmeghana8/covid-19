import pandas as pd
import numpy as np
import json
import sys
import folium
import branca.colormap as cm
sys.path.append('..')


df = pd.read_csv('data/rt_datewise.csv')
df1 = df[['date', 'state', 'ML']]
dates = df1.date.unique()
for d in dates:
    df2 = df1[df1['date']==d]
    df2 = df2.replace(['AP', 'BR', 'DL', 'GJ', 'HR', 'JK', 'KA', 'KL', 'MH', 'MP', 'PB',
       'RJ', 'TG', 'TN', 'UP', 'WB'],
        ['Andhra Pradesh',
        'Bihar',
        'Delhi',
        'Gujarat',
        'Haryana',
        'Jammu & Kashmir',
        'Karnataka',
        'Kerala', 'Maharashtra',                                    
        'Madhya Pradesh',
        'Punjab',
        'Rajasthan',
        'Telangana',  
        'Tamil Nadu',
        'Uttar Pradesh',
        'West Bengal'])
    
    geo_json_data = json.load(open('data/india/state/india_telengana.geojson'))
    rate_dict = df2.set_index('state')['ML']
    added_list = ['Andhra Pradesh',
                    'Bihar',
                    'Delhi',
                    'Gujarat',
                    'Haryana',
                    'Jammu & Kashmir',
                    'Karnataka',
                    'Kerala', 
                    'Maharashtra',                                    
                    'Madhya Pradesh',
                    'Punjab',
                    'Rajasthan',
                    'Telangana',  
                    'Tamil Nadu',
                    'Uttar Pradesh',
                    'West Bengal']
    
    i = 0
    for key in geo_json_data['features']:
        if geo_json_data['features'][i]['properties']['NAME_1'] not in added_list:
            st = geo_json_data['features'][i]['properties']['NAME_1']
            rate_dict[st] = 0
            i = i+1
        
    m = folium.Map(location=[21, 78], tiles='cartodbpositron', zoom_start=4)
    
    lin = cm.LinearColormap(['#004d00','#00cc00','#ffd9b3','#ff6966',
                            '#e60400','#ff0400', '#660000'], 
                            index = [0,0.5,0.7,0.9,1.2,1.5,3.5], vmin=0, vmax=6)    
    

