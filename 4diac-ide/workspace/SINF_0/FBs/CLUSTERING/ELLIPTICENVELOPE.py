import numpy as np
import numpy as np
from sklearn.covariance import EllipticEnvelope


class ELLIPTICENVELOPE:
    def __init__(self):
        self.store_precision = True
        self.assume_centered = False
        self.support_fraction = None
        self.contamination = 0.1
        self.random_state = None

    def schedule(self, event_input_name, event_input_value, pickle, data_in, store_precision, assume_centered, support_fraction, contamination, r_state):
        if event_input_name == 'INIT':
            return [None, None,
                    None, None, None, None, None, None, None, None, None, None, None]

        elif event_input_name == 'RUN':

            if pickle is None:

                self.full_data = np.array(np.copy(data_in))

                # default values or not
                if store_precision is not None:
                    if store_precision == 'True':
                        self.store_precision = True
                    elif store_precision == 'False':
                        self.store_precision = False
                if assume_centered is not None:
                    if assume_centered == 'True':
                        self.assume_centered = True
                    elif assume_centered == 'False':
                        self.assume_centered = False
                if support_fraction is not None:
                    self.support_fraction = float(support_fraction)
                if contamination is not None:
                    self.contamination = float(contamination)
                if r_state is not None:
                    self.random_state = int(r_state)

                model = EllipticEnvelope(store_precision = self.store_precision,
                                          assume_centered = self.assume_centered,
                                          support_fraction = self.support_fraction,
                                          contamination = self.contamination,
                                          random_state=self.random_state).fit(self.full_data)

                return [None, event_input_value, model,
                        None, model.location_, model.covariance_, model.precision_, model.support_, None, model.raw_location_, model.raw_covariance_, model.raw_support_, model.dist_]

            else:
                self.full_data = np.matrix(np.copy(data_in))
                print("Sample to predict:" , self.full_data)

                model = pickle
                results = model.predict(self.full_data)
                prediction = results[0]

                return [None, event_input_value, model,
                        prediction, model.location_, model.covariance_, model.precision_, model.support_, None, model.raw_location_, model.raw_covariance_, model.raw_support_, model.dist_]