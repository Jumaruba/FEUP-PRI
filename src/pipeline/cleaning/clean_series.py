import json

series_raw = open("../../data/raw/series.json" ,"r")
series_clean = open("../../data/clean/series.json" ,"w")

series_list = []
drop_keys = ('primary_work_count','note','numbered')
for serie_obj in series_raw: 
    serie = json.loads(serie_obj)
    [serie.pop(drop_key, None) for drop_key in drop_keys]
    series_list.append(serie)

json.dump(series_list, series_clean, indent=2)
series_raw.close()
series_clean.close()