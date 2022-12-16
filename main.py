import argparse

list_for_strochka = []
def task1(filenamee,countryy,yearr):
    people_count = 0
    # is_first_line = True
    with open(filenamee, "r") as file:
        head = file.readline()
        # if is_first_line:
        linee = file.readline()
        if linee != "":
            resultfile = open(args.output, "w")

            while people_count < 10:
                line = linee.split("\t")
                country = line[7]
                name = line[1]
                year = line[9]
                medals = line[14]
                sport = line[12]
                if yearr == year and countryy == country:
                    if medals != "NA\n":
                        people_count += 1
                        print(f"{name} - {sport} - {medals}")
                        list_for_strochka.append((f"{name} - {sport} - {medals}"))
                        if args.output != None:
                            resultfile.write(f"{name} - {sport} - {medals}")

                linee = file.readline()
        # is_first_line = False

parser = argparse. ArgumentParser(description="")
parser.add_argument("filename")
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", required=False)

args = parser.parse_args()
medals = args.medals
countryy = args.country
yearr = args.year
filenamee = args.filename
newfile = args.output


print(countryy, yearr)
print(f"{args.filename=}")
print(args)
if medals == True:
    task1(filenamee, countryy, yearr)




