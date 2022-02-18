def my_map(data_list):
    for elem in data_list:
        if isinstance(elem, list):
            for further_elem in my_map(elem):
                yield further_elem
        else:
            yield elem


class FlatIterator:
    def __init__(self, data):
        self.data = list(my_map(data))
        self.index = 0

    def __iter__(self):
        self.cursor = self.index - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.data):
            raise StopIteration
        return self.data[self.cursor]


def flat_generator(data):
    data = list(my_map(data))
    index = 0
    while index < len(data):
        yield data[index]
        index += 1


if __name__ == '__main__':
    # Example of Nested List
    nested_list = ['a', ['a', 'b', ['c', ['a']]], ['d', 'e', 'f', 'h', False], [1, 2, None]]

    # Flat Iterator
    print('Flat Iterator:', end=' ')
    for item in FlatIterator(nested_list):
        print(item, end=' ')
    print([item for item in FlatIterator(nested_list)])

    # Flat Generator
    print('Flat Generator:', end=' ')
    for item in flat_generator(nested_list):
        print(item, end=' ')
