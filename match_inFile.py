import csv
import re

def content_of_file(file, w):
    with open(file, 'r') as csv_file:
        lines = csv.DictReader(csv_file)
        string = ' '.join([str(word) for word in lines])

    regex = re.search(w, string)
    print(regex)

print(content_of_file("text.csv", 'text'))