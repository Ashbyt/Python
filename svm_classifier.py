import numpy as np
from sklearn import svm
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.cross_validation import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import label_binarize
import argparse
from scipy.sparse.csr import csr_matrix

def load_sparse_matrix(input_file_path):
    data = np.loadtxt(input_file_path, delimiter = ',')
    return csr_matrix(( data[:,2], (data[:,0], data[:,1])  ) )


def classifyPatents(feature_vectors, labels):
    
    test_proportion = 0.3
    labels = label_binarize(labels,classes= ['A','B','C','D','E','F','G','H'])
    random_state = np.random.RandomState(0)
    X_train, X_test, y_train, y_test = train_test_split(feature_vectors, labels, test_size = test_proportion,
                                                        random_state=random_state)
    classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,
                                 random_state=random_state))
    y_score = classifier.fit(X_train, y_train).decision_function(X_test)

    n_classes = 8
    # Compute Precision-Recall and plot curve
    precision = dict()
    recall = dict()
    average_precision = dict()
    for i in range(n_classes):
        precision[i], recall[i], _ = precision_recall_curve(y_test[:, i], y_score[:, i])
        average_precision[i] = average_precision_score(y_test[:, i], y_score[:, i])

    # Compute micro-average ROC curve and ROC area
    precision["micro"], recall["micro"], _ = precision_recall_curve(y_test.ravel(),
        y_score.ravel())
    average_precision["micro"] = average_precision_score(y_test, y_score,
                                                         average="micro")
    
        
    print 'AUC={0:0.2f}'.format(average_precision['micro'])


parser = argparse.ArgumentParser(description='get AUC score')

parser.add_argument('feature_vector_file', help = 'file path of feature vectors')

parser.add_argument('label_file', help = 'file path of labels')

args = parser.parse_args()

if __name__ == '__main__':
    
    label_file = open(args.label_file, 'r')

    labels = label_file.readlines()
    
    labels = [l.rstrip().split(',')[1] for l in labels]
    
    feature_vectors = load_sparse_matrix(args.feature_vector_file)
    
    classifyPatents(feature_vectors, labels)    
    
    label_file.close()
        
    





