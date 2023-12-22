
class Extract():
    """Extracts data from the pandas data frame"""

    def __init__(self, job, data):
        self.job = job
        self.data = data

    def get_required_data(self): # Extract specific data defined in job.
        result = dict()
        main_list = list()
        data = self.data
        i = 0
        while i < len(data): # Loop over main dataframe.
            for key, value in self.job.items(): # For every specified job, add key value to dict.
                if key in data:
                    result[value] = data.iloc[i][key]
            main_list.append(result)
            i += 1

        return main_list
