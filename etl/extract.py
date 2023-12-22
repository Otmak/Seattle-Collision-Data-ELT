
class Extract():
    """Extracts data and formats it to an array of dicts"""

    def __init__(self, job, data):
        self.job = job
        self.data = data

    def get_required_data(self):
        result = dict()
        my_list = list()
        data = self.data
        i = 0
        while i < len(data):
            for key, value in self.job.items():
                if key in data:
                    result[value] = data.iloc[i][key]
            my_list.append(result)
            i += 1

        return my_list
