import pandas as pd


def read_csv(filepath):
    df = pd.read_csv(filepath,header=None, encoding='latin-1')
    return df

def give_column_name(df):
    newColumn ={0: 'Class',1: 'cap_shape',2: 'cap_surface',3: 'cap_color',4: 'isBruised',5:'odor',6:'gill_attachment',7:'gill_spacing',8:'gill_size',9:'gill_color',10:'stalk_shape',11:'stalk_root',12:'stalk_surface_above_ring',
13:'stalk_surface_below_ring',
14:'stalk_color_above_ring',
15:'stalk_color_below_ring',
16:'veil_type',
17:'veil_color',
18:'ring_number',
19:'ring_type',
20:'spore_print_color',
21:'population',
22:'habitat'}
    df = df.rename(columns=newColumn)

    return df

def convert_to_csv(df):
    df.to_csv('data/agaricus-lepiota.csv', index=False)
    return df



