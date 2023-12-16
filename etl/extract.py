class Extract():
    """docstring for Extract"""

    def __init__(self, job, data):
        self.job = job
        self.data = data

    def get_required_data(self, job, data):
        result = dict()
        my_list = list()
        i = 0
        while i < len(data):
            for key, value in job.items():
                if key in data:
                    result[value] = data.iloc[i][key]
            my_list.append(result)
            print(result)
            i += 1

        return my_list
