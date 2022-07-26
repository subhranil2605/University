# 1. Read the dataset
def read_dataset(filename: str):
    with open(filename) as f_obj:
        for row in f_obj.readlines():
            yield row


# 2. Print the dataset as output
def print_dataset(filename: str) -> None:
    [print(row) for row in read_dataset(filename)]


# 3. Count the number of rows
def count_rows(filename: str):
    return sum([1 for _ in read_dataset(filename)])


# 4. Count the number of columns
def count_cols(filename: str) -> None:
    data = read_dataset(filename)
    [print(len(d.split(','))) for i, d in enumerate(data) if i == 0]


# 5. Print the first row (column label)
def column_names(filename: str) -> list[str]:
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
    classes = {}
    for i in read_dataset(filename):
        for c in unique_class(filename):
            if i.split(',')[-1].strip() == c:
                classes.setdefault(c, []).append(i)

    return classes


if __name__ == '__main__':
    # reading the dataset
    # dataset = read_dataset('dlbcl-fl.csv')

    # print the dataset
    # print_dataset('dlbcl-fl.csv')

    # count rows
    print(count_rows('dlbcl-fl.csv'))

    # a = split_dataset('dlbcl-fl.csv')
    #
    # for class_name in a.keys():
    #     print(f"The number of values in class '{class_name}' is: {len(a[class_name])}")
