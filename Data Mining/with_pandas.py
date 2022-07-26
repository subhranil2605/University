with open('dlbcl-fl.csv') as f:
    data = f.read()

column_names = data.split('\n')[0]

rows = data.split('\n')[1:]

for i in range(5):
    print(rows[i])
