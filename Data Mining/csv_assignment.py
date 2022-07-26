class CsvNil:
    def __init__(self, filename: str):
        self.filename = filename

    def read_dataset(self):
        """ Read the csv file """
        with open(self.filename) as f_obj:
            for row in f_obj.readlines():
                yield row

    def print_dataset(self) -> None:
        """ Print the csv file """
        [print(row) for row in self.read_dataset()]

    def count_rows(self) -> int:
        """ Count the number of rows """
        return sum([1 for _ in self.read_dataset()])

    def count_cols(self) -> int:
        """ Count the number of columns """
        return [len(d.split(',')) for i, d in enumerate(self.read_dataset()) if i == 0][0]

    def column_names(self):
        """ Print the first row (column label) """
        return [d.split(',') for i, d in enumerate(self.read_dataset()) if i == 0][0]

    def first_row(self):
        """ Print the first row (without column label) """
        return [d.split(',') for i, d in enumerate(self.read_dataset()) if i == 1][0]

    def last_column_label(self) -> str:
        """ Print the last column (class label) """
        return self.column_names()[-1].strip()

    def last_column(self) -> list:
        """ Print the last column (without class label) """
        return [d.split(',')[-1].strip() for i, d in enumerate(self.read_dataset()) if i != 0]

    def unique_class(self) -> list:
        """ Print the unique class label """
        return list(set(self.last_column()))

    def split_dataset(self) -> dict:
        """ Divide the dataset into class labels """
        classes = {}
        for row in self.read_dataset():
            for clss in self.unique_class():
                if row.split(',')[-1].strip() == clss:
                    classes.setdefault(clss, []).append(row)

        return classes


if __name__ == '__main__':
    """# 1. Read the CSV"""

    csvnil = CsvNil('dlbcl-fl.csv')

    """# 2. Print the CSV"""

    print(csvnil.print_dataset())

    """# 3. Count the number of rows"""

    print(csvnil.count_rows() - 1)

    """# 4. Count the number of columns"""

    print(csvnil.count_cols())

    """# 5. Print the first row (column label)"""

    print(csvnil.column_names())

    """# 6. Print the first row (without column label)"""

    print(csvnil.first_row())

    """# 7. Print the last column (class label)"""

    print(csvnil.last_column_label())

    """# 8. Print the last column (without class label)"""

    print(csvnil.last_column())

    """# 9. Print the unique class label"""

    print(csvnil.unique_class())

    """# 10. Divide the dataset into class labels"""

    split_data_dict: dict = csvnil.split_dataset()

    print(split_data_dict)

    dlbcl = split_data_dict['DLBCL']
    fl = split_data_dict['FL']

    print(len(dlbcl))

    print(len(fl))
