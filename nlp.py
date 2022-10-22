import re
import string
import pandas as pd
from pdf_reader import extract
from sklearn.feature_extraction.text import TfidfVectorizer
def clean_text_round1(text):
    '''Make text lowercase, remove punctuation and remove words containing numbers and stopwords.'''
    text = text.lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    with open('stopwords.txt') as f:
        stopwords = []
        for line in f:
            print(line)
            stopwords.append(line)
        for stopword in stopwords:
            text = re.sub(stopword, '', text)
    return text

def transform_row(filename):
    text = extract(filename)
    text = clean_text_round1(text)
    return text


def cluster_text(text):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    Sum_of_squared_distances = []
    K = range(2, 10)
    for k in K:
        km = KMeans(n_clusters=k, max_iter=200, n_init=10)
        km = km.fit(X)
        Sum_of_squared_distances.append(km.inertia_)
    plt.plot(K, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()

    print('How many clusters do you want to use?')
    true_k = int(input())
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
    model.fit(X)

    labels = model.labels_
    clusters = pd.DataFrame(list(zip(text, labels)), columns=['title', 'cluster'])
    # print(clusters.sort_values(by=['cluster']))

    for i in range(true_k):
        print(clusters[clusters['cluster'] == i])

    return
if __name__ == "__main__":
    df = pd.read_csv('misie_KIID_META.csv')
    df['clean_text'] = df.apply(lambda row: transform_row(row['NAZWA_PLIKU']), axis=1)

    round1 = lambda x: clean_text_round1(x)

