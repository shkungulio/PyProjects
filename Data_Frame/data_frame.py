#!/bin/env/ python3

import pandas

visitors = [1234, 2345, 3456, 4567, 5678]
errors = [34, 45, 56, 67, 78]

df = pandas.DataFrame({"Visitors": visitors, "Errors": errors},
index=["Mon", "Tue", "Wed", "Thu", "Fri"])

print(df)