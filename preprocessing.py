from sklearn.model_selection import train_test_split

def split_features(df):
    X = df.drop(['target'], axis=1)
    y = df['target']
    return X, y

def create_train_test_split(X, y, test_size=0.2, random_state=5):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
