import pandas as pd
from mdutils import MdUtils
import os 

def stats(df: pd.DataFrame, md: MdUtils) -> None:
    md.new_header(level=1, title='General Statistics')

    md.new_header(level=2, title='Data Types')
    data_types = df.dtypes
    data_types_df = pd.DataFrame({'Column':data_types.index, 'Data Type':data_types.values})
    md.write(data_types_df.to_markdown(index=False), wrap_width=0)
    md.write('\n')

    md.new_header(level=2, title='Null Count')
    nulls = df.isnull().sum()
    nulls_df = pd.DataFrame({'Column':nulls.index, 'Null Count':nulls.values})
    md.write(nulls_df.to_markdown(index=False), wrap_width=0)
    md.write('\n')
    
    md.new_header(level=2, title='Unique Values')
    unique_values = df.nunique()
    unique_values_df = pd.DataFrame({'Column':unique_values.index, 'Unique Count':unique_values.values})
    md.write(unique_values_df.to_markdown(index=False), wrap_width=0)
    md.write('\n')



def get_processed_filepath(filename: str) -> str:
    return get_full_path('../../data/combine/') + filename


def get_explore_filepath(filename: str) -> str:
    return get_full_path("../../data/explore/") + filename


def get_plots_filepath(filename: str) -> str: 
    return get_plots_path() + filename


def get_plots_path() -> str:
    return get_full_path('../../data/explore/plots/' )


def get_full_path(path: str) -> str:
    current_path =  os.path.dirname(os.path.abspath(__file__)) + "/../" 
    return current_path + path


