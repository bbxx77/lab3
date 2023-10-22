class DataAdapter:
    def __init__(self, data_source):
        self.data_source = data_source

    def get_data(self):
        data = self.data_source.get_data_dict()
        if isinstance(data, dict):
            return data
        elif isinstance(data, list):
            return {
                "name": data[0],
                "age": data[1],
            }
        else:
            return {}
