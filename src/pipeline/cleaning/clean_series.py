import json
import csv

def clean_series():
    series_raw = open("../../data/raw/series.json" ,"r")
    series_clean = open("../../data/clean/series.csv" ,"w", newline="\n", encoding="utf-8")
    writer = csv.writer(series_clean)

    header = ["description", "title", "series_works_count", "series_id"]
    writer.writerow(header)

    for serie_obj in series_raw: 
        serie = json.loads(serie_obj)
        serie.pop('primary_work_count', None)
        serie.pop('note', None)
        serie.pop('numbered', None)
        writer.writerow(serie.values())

    series_raw.close()
    series_clean.close()

if __name__ == '__main__':
    clean_series()