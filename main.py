import argparse

def task1(filenamee,countryy,yearr):
    head = None
    is_first_line = True
    with open(filenamee, "r") as file:
        for line in file.readlines():
            if is_first_line:
                head = line.split("\t")
                is_first_line = False
                continue

            head.index("NOC")

parser = argparse. ArgumentParser(description="")
parser.add_argument("filename")
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
args = parser.parse_args()
countryy = args.country
yearr = args.year
filenamee = args.filename

print(countryy, yearr)
print(f"{args.filename=}")
print(args)
if medals == True:
