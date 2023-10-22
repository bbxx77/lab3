from d_display import DataDisplay

class ConsoleDataDisplay(DataDisplay):
    def show_data(self, data):
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
