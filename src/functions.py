import csv
import decimal
import datetime

def create_lists():

    '''Returns two lists alphabetically sorted in reverse. One contains the types of border.
       The other one contains the means of crossing the border.'''

    borders = set()
    transports = set()

    with open('./input/Border_Crossing_Entry_Data.csv', 'r') as csv_file:

        reader = csv.reader(csv_file, delimiter = ',') 

        #skips header
        next(reader)

        for row in reader:
            borders.add(row[3])
            transports.add(row[5])      

    b = list(borders)
    t = list(transports)
    b.sort(reverse=True)
    t.sort(reverse=True)

    return(b, t)


def create_transport_matrix(border, transport):

    '''Returns a matrix containing only the information of the input border
       and the input mean of transportation.'''

    border_arr = []

    with open('./input/Border_Crossing_Entry_Data.csv', mode='r') as csv_file:

        reader = csv.reader(csv_file, delimiter=',')

        #skips header
        next(reader)

        for row in reader:

            if(row[3] == border) and (row[5] == transport):
                border_arr.append(row)
    
    return border_arr
    


def total_crossings(array):

    '''Returns a dictionary containing unique dates as keys and
	   the total number of border crossings for that date.'''
		
    dictionary = {}

    for i in range(len(array)):

        if array[i][4] in dictionary:
            dictionary[array[i][4]] = dictionary[array[i][4]] + int(array[i][6])
        else:
            dictionary[array[i][4]] = int(array[i][6])

    return dictionary
    


def running_averages(dictionary):

    '''Returns a list containing the running averages for the input dictionary.'''

    crossings = list(dictionary.values())

    averages = []
    
    runAverage = 0
    total = 0
    items = 0

    for i in reversed(crossings):

        avgDec = decimal.Decimal(runAverage).quantize(decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP)

        averages.insert(0, avgDec)

        total += int(i)
        items += 1
        runAverage = total / items

    return averages


def sort_by_date(reader):

<<<<<<< HEAD
    '''Creates a csv file with the same rows in reader but sorted by date.'''
=======
    '''Creates a csv file with the rows in reader but sorted by date.'''
>>>>>>> 0b464750f38c00fd8293785291c119a2a26d36eb
        
    with open('./output/report.csv', 'w', newline='') as csv_final:
                        
        header = ['Border', 'Date', 'Measure', 'Value', 'Average']

        writer = csv.writer(csv_final)
        
        writer.writerow(header)
        writer.writerows(sorted(reader,
            key=lambda row: datetime.datetime.strptime(row[1], '%m/%d/%Y %H:%M:%S %p'), reverse=True))
    
