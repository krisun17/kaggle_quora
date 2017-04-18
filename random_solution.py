import csv
from random import random

test_set_size = 2345796

with open("./data/solution.csv", "w") as f:
    fieldnames = ['test_id', 'is_duplicate']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(test_set_size):
        writer.writerow({"test_id": i, "is_duplicate": "{0:.2f}".format(random())})
