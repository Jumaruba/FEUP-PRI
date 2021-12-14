# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd

metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f) 

# RECALL =====================================
@metric
def recall(results, relevant, id_fieldname):
    """ 
    Calculates the recall for the documents. 
    Formula: Number of relevant documents retrieved / total relevant documents.
    """
    return len([
        doc 
        for doc in results
        if (int(doc[id_fieldname])) in relevant
    ]) / len(relevant) 
    
# AVERAGE PRECISION ==========================
@metric
def ap(results, relevant, id_fieldname):
    """
    Calculates teh average precision. 
    Source: https://towardsdatascience.com/breaking-down-mean-average-precision-map-ae462f623a52 
    """
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if int(doc[id_fieldname]) in relevant
        ]) / idx 
        for idx in range(1, len(results)+1)
    ] 

    return sum(precision_values)/len(precision_values) 
    
# P5 ============================================ 
@metric
def p5(results, relevant, id_fieldname):
    return len([doc for doc in results[:5] if int(doc[id_fieldname]) in relevant])/5

def calculate_metric(key, results, relevant, id_fieldname):
    return metrics[key](results, relevant, id_fieldname)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p5': 'Precision at 5 (P@5)',
    'recall': 'Recall metric'
}


def generate_metrics(results, relevant, id_fieldname):
    # Calculate all metrics and export results as LaTeX table
    df = pd.DataFrame([['Metric','Value']] +
        [
            [evaluation_metrics[m], calculate_metric(m, results, relevant, id_fieldname)]
            for m in evaluation_metrics
        ]
    )

    with open('results.tex','w') as tf:
        tf.write(df.to_latex())

    # PRECISION-RECALL CURVE =================================================
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
    print("==== titles ===")
    for doc in results:
        print(doc['title'])
    print("==== recall ====")
    print(recall(results, relevant, id_fieldname))


    disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
    disp.plot()
    plt.savefig('precision_recall.pdf')

