import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def plot_map(cr, yr):
    print('bharathraj')
    print(yr)
    fp = r"map\output.shp"
    map = gpd.read_file(fp)
    mp_df = pd.read_csv('final.csv')
    df = mp_df
    

    ladakh_present = 'LADAKH' in df['STATE/UT'].values
    telangana_present = 'TELANGANA' in df['STATE/UT'].values
    years = list(range(2001, 2015))

    states = ['A & N ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR',
           'CHANDIGARH', 'CHHATTISGARH', 'D & N HAVELI', 'DAMAN & DIU', 'GOA',
           'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH', 'JHARKHAND', 'KARNATAKA',
           'KERALA', 'LAKSHADWEEP', 'MADHYA PRADESH', 'MAHARASHTRA',
           'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'DELHI UT',
           'PUDUCHERRY', 'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU',
           'TELANGANA', 'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND',
           'WEST BENGAL', 'ODISHA', 'ANDHRA PRADESH', 'JAMMU & KASHMIR',
           'LADAKH'] if not ladakh_present else ['A & N ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR',
           'CHANDIGARH', 'CHHATTISGARH', 'D & N HAVELI', 'DAMAN & DIU', 'GOA',
           'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH', 'JHARKHAND', 'KARNATAKA',
           'KERALA', 'LAKSHADWEEP', 'MADHYA PRADESH', 'MAHARASHTRA',
           'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'DELHI UT',
           'PUDUCHERRY', 'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU',
           'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND',
           'WEST BENGAL', 'ODISHA', 'ANDHRA PRADESH', 'JAMMU & KASHMIR'] if not telangana_present else ['A & N ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR',
           'CHANDIGARH', 'CHHATTISGARH', 'D & N HAVELI', 'DAMAN & DIU', 'GOA',
           'GUJARAT', 'HARYANA', 'HIMACHAL PRADESH', 'JHARKHAND', 'KARNATAKA',
           'KERALA', 'LAKSHADWEEP', 'MADHYA PRADESH', 'MAHARASHTRA',
           'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'DELHI UT',
           'PUDUCHERRY', 'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU',
           'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND',
           'WEST BENGAL', 'ODISHA', 'ANDHRA PRADESH', 'JAMMU & KASHMIR']

    add = pd.DataFrame([(state, year) for state in states for year in years], columns=['STATE/UT', 'YEAR'])
    add['MURDER'] = 0
    add['RAPE'] = 0
    add['THEFT'] = 0
    add['OTHER IPC CRIMES'] = 0
    add['TOTAL IPC CRIMES'] = 0
    add['KIDNAPPING & ABDUCTION'] = 0

    if not ladakh_present or not telangana_present:
        mp_df = pd.concat([mp_df, add], ignore_index=True)
    else:
        mp_df = mp_df.copy()

    
    m_df = mp_df[mp_df['YEAR'] == yr]
    try:
        m_df = m_df.drop(['DISTRICT'], axis=1)
        m_df = m_df.groupby(['STATE/UT', 'YEAR']).sum().reset_index()
    except:
        print("nope")
    m_df.rename(columns={'MURDER': 'murder', 'RAPE': 'rape', 'KIDNAPPING & ABDUCTION': 'kidnap', 'THEFT': 'theft', 'OTHER IPC CRIMES': 'other', 'TOTAL IPC CRIMES': 'total_ipc'}, inplace=True)
    mp_df.rename(columns={'MURDER': 'murder', 'RAPE': 'rape', 'KIDNAPPING & ABDUCTION': 'kidnap', 'THEFT': 'theft', 'OTHER IPC CRIMES': 'other', 'TOTAL IPC CRIMES': 'total_ipc'}, inplace=True)
    df.rename(columns={'MURDER': 'murder', 'RAPE': 'rape', 'KIDNAPPING & ABDUCTION': 'kidnap', 'THEFT': 'theft', 'OTHER IPC CRIMES': 'other', 'TOTAL IPC CRIMES': 'total_ipc'}, inplace=True)
    mp = map.set_index('st_nm').join(m_df.set_index('STATE/UT'))
    mp.fillna(0, inplace=True)

    fig, ax = plt.subplots(1, figsize=(15, 15))
    ax.axis('off')
    ax.set_title(cr, fontdict={'fontsize': '25', 'fontweight': '10'})

    mp.plot(column=cr, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0', legend=True, markersize=[39.739192, -104.990337])

    plt.savefig('website/images/map_plot.jpg')
    

