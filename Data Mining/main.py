class Csvnil:
    def __init__(self, filename):
        self.filename = filename

    def read_dataset(self):
        with open(self.filename) as f_obj:
            for row in f_obj.readlines():
                yield row

    def print_dataset(self):
        [print(row) for row in self.read_dataset()]


if __name__ == '__main__':
    csvnil = Csvnil('dlbcl-fl.csv')
    csvnil.print_dataset()