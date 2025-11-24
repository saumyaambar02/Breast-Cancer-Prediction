import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

def load_data():
    cancer = load_breast_cancer()
    df = pd.DataFrame(
        np.c_[cancer['data'], cancer['target']],
        columns=np.append(cancer['feature_names'], ['target'])
    )
    return df, cancer
