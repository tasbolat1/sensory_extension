import pickle
import pandas as pd

def read_optitrack(fname):
    optitrack_data = pickle.load(open(fname, 'rb'))
    optitrack_df = pd.DataFrame(columns=['time', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz'],
             data=optitrack_data)
    return optitrack_df