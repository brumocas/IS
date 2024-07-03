import numpy  as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class PCA_TRANSF:

    def __init__(self):
        self.data_in=[]
        self.n_components=0
        self.result=[]
        self.explained=[]
        self.explained_total=[]
        self.size=[]
        self.fit_function=[]

    def schedule(self, event_input_name, event_input_value, features, data_from_pickle):

        if event_input_name == 'INIT':

            return [event_input_value, None, self.result, self.explained, self.explained_total, self.fit_function, self.size]

        elif event_input_name == 'RUN':

            if len(features) == 0:
                return [None, event_input_value, self.result, self.explained, self.explained_total, self.fit_function, self.size]
            else:
                if data_from_pickle == None:
                    self.data_in=np.array(features)
                    pca_2 = PCA(0.95)
                    self.fit_function = pca_2.fit(self.data_in)
                    self.result = pca_2.transform(self.data_in)
                    self.explained = np.array(pca_2.explained_variance_ratio_)
                    self.explained_total = np.cumsum(self.explained)[-1]
                    self.size = self.result.shape
                    return [None, event_input_value, self.result, self.explained, self.explained_total, self.fit_function, self.size]

                else:
                    self.data_in = np.array(features)
                    pca=data_from_pickle
                    self.fit_function = data_from_pickle
                    self.result = pca.transform(np.reshape(self.data_in, (1, -1)))
                    self.explained = np.array(pca.explained_variance_ratio_)
                    self.explained_total = np.cumsum(self.explained)[-1]
                    self.size = self.result.shape
                    return [None, event_input_value, *self.result, self.explained, self.explained_total,
                            self.fit_function, self.size]