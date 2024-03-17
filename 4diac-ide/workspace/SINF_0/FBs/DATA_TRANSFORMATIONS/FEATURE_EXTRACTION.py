import numpy as np


class FEATURE_EXTRACTION:

    def __init__(self):
        self.data_in = []
        self.data_out = []
        self.width = 0
        self.size = []
        self.ndim = 0

    def schedule(self, event_input_name, event_input_value, data_in, depth):
        if event_input_name == 'INIT':

            return [event_input_value, None, self.data_out, self.size]

        elif event_input_name == 'RUN':
            self.all_data_in = np.copy(data_in)
            n_fea = len(self.all_data_in)

            self.depth = float(depth)
            self.data_out = []

            #evaluates the number of dimensions of the inputted data. If it is a line, behaves as follow. If it is a matrix, see "else:"
            for i in range(n_fea):
                #calculates the number of measurements per line
                self.data_in = self.all_data_in[i]
                self.width = len(self.data_in[0])

                #calculates the mean values for the: entire window, half window and a quarter of window (takes the most recent values)
                mean_x = np.mean(self.data_in[:,-1: (-self.width - 1):-1], axis=1)
                mean_x_2 = np.mean(self.data_in[:,-1: (-int(self.width / self.depth) - 1):-1], axis=1)
                mean_x_4 = np.mean(self.data_in[:,-1: (-int(self.width / (self.depth*2)) - 1):-1], axis=1)

                if len(self.data_out) == 0:
                    self.data_out = mean_x.reshape(-1,1)
                else:
                    self.data_out = np.hstack((self.data_out, mean_x.reshape(-1,1)))
                self.data_out = np.hstack((self.data_out, mean_x_2.reshape(-1,1)))
                self.data_out = np.hstack((self.data_out, mean_x_4.reshape(-1,1)))

                #calculates the std values for the: entire window, half window and a quarter of window (takes the most recent values)
                std_x = np.std(self.data_in[:,-1: (-self.width - 1):-1], axis=1)
                std_x_2 = np.std(self.data_in[:,-1: (-int(self.width / self.depth) - 1):-1], axis=1)
                std_x_4 = np.std(self.data_in[:,-1: (-int(self.width / (self.depth*2)) - 1):-1], axis=1)

                self.data_out = np.hstack((self.data_out, std_x.reshape(-1,1)))
                self.data_out = np.hstack((self.data_out, std_x_2.reshape(-1,1)))
                self.data_out = np.hstack((self.data_out, std_x_4.reshape(-1,1)))

                #calculates the shape of the output

            self.size = np.shape(self.data_out)

            return [None, event_input_value, self.data_out, self.size]