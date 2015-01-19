import csv
import sys

def add_cities(ifile, ofile):
  ifile = open(ifile, "r")
  ofile = open(ofile, "a")

  reader = csv.reader(ifile)
  writer = csv.writer(ofile)

  for row in reader:
    print row[2]
    if "," in row[2]:
      city = row[2].split(",")[0].strip()
    else:
      city = row[2]
      
    row.append(city)
    row.append("end")
    print row      
    writer.writerow(row)    


if __name__ == "__main__":

  add_cities(sys.argv[1], sys.argv[2])


