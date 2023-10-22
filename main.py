from d_data_source import DictionaryDataSource
from l_data_source import ListDataSource
from data_adapter import DataAdapter
from console_d_display import ConsoleDataDisplay

if __name__ == "__main__":
    dictionary_data_source = DictionaryDataSource()
    list_data_source = ListDataSource()

    dictionary_adapter = DataAdapter(dictionary_data_source)
    list_adapter = DataAdapter(list_data_source)

    data_display = ConsoleDataDisplay()

    print("Display data from a dictionary:")
    dictionary_data = dictionary_adapter.get_data()
    data_display.show_data(dictionary_data)

    print("\nDisplay data from a list:")
    list_data = list_adapter.get_data()
    data_display.show_data(list_data)
