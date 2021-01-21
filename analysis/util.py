import pickle
import pandas as pd
import numpy as np

def read_optitrack(fname):
    optitrack_data = pickle.load(open(fname, 'rb'))
    optitrack_df = pd.DataFrame(columns=['time', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz'],
             data=optitrack_data)
    return optitrack_df

def read_biotac(fname, time_nullified = False):
    data = pickle.load(open(fname, 'rb'))
    columns = ['t', 'tdc', 'tac', 'pdc', 'pac', 'el']
    df = pd.DataFrame(data=data, columns=columns)
    df_el = pd.DataFrame(df.el.to_list(), index=df.index).add_prefix('el_').astype(int)
    df_pac = pd.DataFrame(df.pac.to_list(), index=df.index).add_prefix('pac_').astype(int)
    if time_nullified:
        df.t = df.t-df.t[0]
    return df.join(df_el).join(df_pac)

def time_interp(t):
    time_list = []
    for i in range(len(t)-1):
        time_list += list(np.linspace(t[i], t[i+1], 23))[:22]
    return time_list