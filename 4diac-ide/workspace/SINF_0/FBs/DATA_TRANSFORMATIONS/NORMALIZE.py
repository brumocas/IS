import numpy  as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class NORMALIZE:

    def __init__(self):
        self.data_in = []
        self.data_scaled = []
        self.fit_function=[]
        self.size=[]

    def schedule(self, event_input_name, event_input_value, data_in, data_from_pickle):
        if event_input_name == 'INIT':
            return [None, None, None, None, None]

        elif event_input_name == 'RUN':

            print("data_in: " , data_in)

            if data_in is None:
                return [None, None, None, None, None]

            if data_from_pickle == None:
                self.data_in = np.copy(data_in)
                my_scaler = StandardScaler()
                my_scaler.fit(self.data_in)
                self.fit_function = my_scaler
                self.data_scaled = my_scaler.transform(self.data_in)
                self.size = self.data_scaled.shape
                return [None, event_input_value, self.data_scaled, self.fit_function, self.size]
            else:
                self.data_in = np.array(np.copy(data_in))
                self.fit_function = data_from_pickle
                my_scaler = data_from_pickle
                self.data_scaled = my_scaler.transform(np.reshape(self.data_in, (1, -1)))
                self.size = self.data_scaled.shape
                return [None, event_input_value, *self.data_scaled, self.fit_function, self.size]