import pandas as pd

def stats(df, md):
    md.new_header(level=1, title='General Statistics')

    md.new_header(level=2, title='Descriptive Analysis')
    md.write(df.describe().to_markdown(), wrap_width=0)
    md.write('\n')

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
