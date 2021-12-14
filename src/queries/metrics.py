# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd
import os

metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f) 

# RECALL
@metric
def recall(results, relevant, id_fieldname):
    return len([
        doc 
        for doc in results
        if (int(doc[id_fieldname])) in relevant
    ]) / len(relevant) 
    

@metric
def ap(results, relevant, id_fieldname):
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if int(doc[id_fieldname]) in relevant
        ]) / idx 
        for idx in range(1, len(results))
    ] 
    return sum(precision_values)/len(precision_values)

@metric
def p5(results, relevant, id_fieldname, n=5):
    return len([doc for doc in results[:n] if int(doc[id_fieldname]) in relevant])/n

def calculate_metric(key, results, relevant, id_fieldname):
    return metrics[key](results, relevant, id_fieldname)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p5': 'Precision at 5 (P@5)',
    'recall': 'Recall metric'
}


def generate_metrics(results, relevant, id_fieldname, path):
    path = "evaluation_results/" + path
    if not os.path.exists(path):
        os.makedirs(path)

    # Calculate all metrics and export results as LaTeX table
    df = pd.DataFrame([['Metric','Value']] +
        [
            [evaluation_metrics[m], calculate_metric(m, results, relevant, id_fieldname)]
            for m in evaluation_metrics
        ]
    )#query_exe(QUERY_BOOKS_3, BOOKS_QRELS_FILEPATH, "book_id","tematic/genres")

    with open(path + 'results.tex','w') as tf:
        tf.write(df.to_latex())

    # PRECISION-RECALL CURVE
    # Calculate precision and recall values as we move down the ranked list
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if int(doc[id_fieldname]) in relevant
        ]) / idx 
        for idx, _ in enumerate(results, start=1)
    ] 

    recall_values = [
        len([
            doc for doc in results[:idx]
            if int(doc[id_fieldname]) in relevant
        ]) / len(relevant)
        for idx, _ in enumerate(results, start=1)
    ]

    precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

    # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
    recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
    recall_values = sorted(set(recall_values))

    # Extend matching dict to include these new intermediate steps
    for idx, step in enumerate(recall_values):
        if step not in precision_recall_match:
            if recall_values[idx-1] in precision_recall_match:
                precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
            else:
                precision_recall_match[step] = precision_recall_match[recall_values[idx+1]] 

    print("==== is in relevant ===")
    for doc in results:
        print(int(doc[id_fieldname]) in relevant)
    print("=== retrieved docs ===")
    for doc in relevant:
        print(doc)
    print("==== recall ====")
    print(recall(results, relevant, id_fieldname))


    disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
    disp.plot()
    plt.savefig(path + 'precision_recall.pdf')
