import csv
import os
import functions as fc


def main():
    
    borderList, transportList = fc.create_lists()
    csv_temp = './output/temp.csv'

    #Creates an unsorted-by-date temp csv file. 
    with open(csv_temp, 'w', newline='') as csv_file:

        writer = csv.writer(csv_file)

        for border in borderList:

            for transport in transportList:
                d = fc.total_crossings(fc.create_transport_matrix(border, transport))

                dates = list(d.keys())
                crossings = list(d.values())
                averages = fc.running_averages(d)

                for i in range(len(d)):
                    writer.writerow([border, dates[i], transport, crossings[i], averages[i]])

    
    #Creates a report.csv from temp csv but sorted by date.
    with open(csv_temp, 'r') as csv_file:

        reader = csv.reader(csv_file)

        fc.sort_by_date(reader)


    os.remove(csv_temp)

if __name__ == "__main__":
	main()