"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

import csv

def sumRows(filename, header=False):
    dic = {}
    with open(filename) as csvfile:
        rdr = csv.reader(csvfile)
        if header == True:
            next(csv.reader(csvfile))
        for row in rdr:
            total = 0
            for col in row[:]:
                if col.isdigit():
                    total += int(col)
            dic[row[0]] = total
    return dic

def sumColumns(filename):
    kobohpjopipojpoj
