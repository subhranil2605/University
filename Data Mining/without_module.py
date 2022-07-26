# 1. Read the dataset
def read_dataset(filename: str):
    with open(filename) as f_obj:
        for row in f_obj.readlines():
            yield row


# 2. Print the dataset as output
def print_dataset(filename: str) -> None:
    [print(row) for row in read_dataset(filename)]


# 3. Count the number of rows
def count_rows(filename: str) -> None:
    number_of_rows: int = 0
    for _ in read_dataset(filename):
        number_of_rows += 1
    print(f"There are {number_of_rows - 1} rows")


# 4. Count the number of columns
def count_cols(filename: str) -> None:
    data = read_dataset(filename)
    [print(len(d.split(','))) for i, d in enumerate(data) if i == 0]


# 5. Print the first row (column label)
def column_names(filename: str) -> list:
    data = read_dataset(filename)
    return [d.split(',') for i, d in enumerate(data) if i == 0][0]


# 6. Print the first row (without column label)
def first_row(filename: str) -> None:
    data = read_dataset(filename)
    [print(d.split(',')) for i, d in enumerate(data) if i == 1]


# 7. Print the last column (class label)
def last_column_label(filename: str):
    return column_names(filename)[-1].strip()


# 8. Print the last column (without class label)
def last_column(filename: str) -> list:
    data = read_dataset(filename)
    return [d.split(',')[-1].strip() for i, d in enumerate(data) if i != 0]


# 9. Print the unique class label
def unique_class(filename: str) -> list:
    return list(set(last_column(filename)))


# 10. Divide the dataset into class labels
def split_dataset(filename: str) -> dict:
    data = read_dataset(filename)
    classes = {}
    for i in data:
        for c in unique_class(filename):
            if i.split(',')[-1].strip() == c:
                classes.setdefault(c, []).append(i)

    return classes


if __name__ == '__main__':
    a = split_dataset('dlbcl-fl.csv')

    for class_name in a.keys():
        print(f"The number of values in class '{class_name}' is: {len(a[class_name])}")
