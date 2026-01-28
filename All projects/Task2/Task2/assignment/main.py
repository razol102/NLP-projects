import json


def classify(train_file, test_file):
    # todo: implement this function
    print(f'starting feature extraction and classification, train data: {train_file} and test: {test_file}')

    # todo: you can try working with various classifiers from sklearn:
    #  https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
    #  https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
    #  https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    #  please use the LogisticRegression classifier in the version you submit

    # todo: fill in the dictionary below with actual scores obtained on the test data
    test_results = {'class_1_F1': 0.0,
                    'class_2_F1': 0.0,
                    'class_3_F1': 0.0,
                    'class_4_F1': 0.0,
                    'class_5_F1': 0.0,
                    'accuracy': 0.0}

    return test_results


if __name__ == '__main__':
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    results = classify(config['train_data'], config['test_data'])

    for k, v in results.items():
        print(k, v)
