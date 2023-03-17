""" Not Part of the framework.
Will be deleted"""
import pandas

df = pandas.read_csv(filepath_or_buffer='../test_data/test_invalid_data.csv', delimiter=';')

print(df)

# print(df.to_string())

print(50 * "-")

print(df.loc[0])

print(50 * "-")

print(df.loc[0].tolist())
print(list(df.loc[0]))
print(tuple(df.loc[0]))

print(50 * "-")

print(df.index)

print(50 * "-")
for i in df.index:
    print(tuple(df.loc[i]))

print(50 * "-")

list = []
for i in df.index:
    list.append(tuple(df.loc[i]))

print(list)

"""can be done in single line by using values property """
print(df.values.tolist())

