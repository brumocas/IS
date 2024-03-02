import numpy as np


class GROUPING:
    def __init__(self):
        self.data_in = []
        self.width = 0
        self.grouped_data = []
        self.step = 0
        self.size=[]

    def schedule(self, event_name, event_value, Feature_column, Width, depth):

        if event_name == 'INIT':

            return [event_value, None, self.grouped_data, self.size]

        elif event_name == 'RUN':
            # assigns a width: given by the user or 20, by default
            if Width is None:
                self.width = 20
            else:
                self.width = int(Width)

            print("depth:" , depth)
            self.depth = float(depth)

            n_row = len(Feature_column)
            n_col = len(Feature_column[0])

            final_final = [0] * n_col

            # defines the step: how many values to jump, each new line
            #self.step = int(self.width / 4)
            self.step = int(self.width / (self.depth*2))

            # inverte a coluna de data, para ficar com a info mais recente em cima, caso tenha de descartar elementos
            self.data_in = Feature_column[-1:-n_row - 1:-1]

            for t in range(n_col):
                self.grouped_data = []
                # creates the groups for each line
                for i in np.arange(0, n_row - self.step + 2, self.step):

                    ans = np.copy(self.data_in[i:(self.width + i), t])

                    if ans.size < self.width:
                        break

                    if len(ans) == self.width:
                        if len(self.grouped_data) == 0:
                            self.grouped_data = np.copy(ans).reshape((1, self.width))
                        else:
                            self.grouped_data = np.vstack((self.grouped_data, ans.reshape((1, self.width))))

                # flips the data, so that chronological order is mantained
                final_final[t] = np.flip(self.grouped_data)

            # evaluates the shape of the output matrix
            self.size = [n_row,len(final_final)]

            return [None, event_value, final_final, self.size]