# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd


# Should be tested with filters and without. 
QRELS_FILE = "../data/queries/tematic/romantic_tragedy.txt"
QUERY_SIMPLE_URL = "http://localhost:8983/solr/books_subset/select?q={!q.op=OR df=description}romantic%26tragedy&q=title:tragedy%26romantic&rows=10&wt=json"
QUERY_BOOST_URL = "http://localhost:8983/solr/books_subset/select?q=({!q.op=OR df=description}romantic%26tragedy)^=4&q=title:tragedy%26romantic&rows=10&wt=json"

results = requests.get(QUERY_BOOST_URL).json()['response']['docs']  
print(len(results))
# Read qrels to extract relevant documents
relevant = list(map(lambda el: int(el.strip()), open(QRELS_FILE).readlines()))
# Get query results from Solr instance

# METRICS TABLE
# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

# RECALL 
def recall(results, relevant):
    return len([
        doc 
        for doc in results
        if (int(doc['book_id'])) in relevant
    ]) / len(relevant) 
    

@metric
def ap(results, relevant):
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if int(doc['book_id']) in relevant
        ]) / idx 
        for idx in range(1, len(results))
    ]
    return sum(precision_values)/len(precision_values)

@metric
def p5(results, relevant, n=5):
    return len([doc for doc in results[:n] if int(doc['book_id']) in relevant])/n

def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p5': 'Precision at 5 (P@5)',
}

# Calculate all metrics and export results as LaTeX table
df = pd.DataFrame([['Metric','Value']] +
    [
        [evaluation_metrics[m], calculate_metric(m, results, relevant)]
        for m in evaluation_metrics
    ]
)

print(df)
with open('results.tex','w') as tf:
    tf.write(df.to_latex())

# PRECISION-RECALL CURVE
# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len([
        doc 
        for doc in results[:idx]
        if int(doc['book_id']) in relevant
    ]) / idx 
    for idx, _ in enumerate(results, start=1)
] 
print("==== is in relevant ===")
for doc in results:
    print(int(doc['book_id']) in relevant)
print("===")
for doc in relevant:
    print(doc)
print("==== recall ====")
print(recall(results, relevant))

recall_values = [
    len([
        doc for doc in results[:idx]
        if int(doc['book_id']) in relevant
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

disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
disp.plot()
plt.savefig('precision_recall.pdf')

