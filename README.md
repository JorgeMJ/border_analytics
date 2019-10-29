TABLE OF CONTENTS:

    0. CONTACT
    1. INTRODUCION
    2. FILE STRUCTURE
    3. SOURCE CODE
    4. RUNNING THE PROGRAM
    5. TESTING



0.- CONTACT:

   Author:  Jorge Martin Joven
   Email:   jmartinjoven@gmail.com
   Github:  https://github.com/JorgeMJ


1.- INTRODUCTION:

   This project calculates the running average of US border-crossings. To do this, the program
uses a csv input file (called 'Border_Crossing_Entry_Data.csv') containg the following fields:
Port Name, State, Port Code, Border, Date, Measure, Value, Location.

The result is an output file (called 'report.csv') containing the following fields:
Border, Date, Measure, Value, Average

In the output file, the meaning of the different fields are:

* Border: can be either US-Canada border or US-Mexico border

* Date: unique date for that kind of border (Border) and that mean of transportation (Measure), regardless
   of the border entry point (Port Name, Port Code or Location)

* Measure: is the way to cross the border (e.g. Pedetrians, Trains, Truck Containers Full,
   Truck Containers Empty...)

* Value: Is the total of border-crossings for a given Border, a given Measure, and a given Date regardless
   of the entry point.

* Average: Represents the running average for a given Border and a given Measure.



The output file rows are sorted in descending order by:
* Date
* Value (or number of crossings)
* Measure
* Border


2-. FILE STRUCTURE: 

( **In this graph folders are enclosed in square brackets. e.g.[folder] )

    +-- README.md
    +-- run.sh
    +-- [src]
    ¦   +-- border_analytics.py
    |   +-- functions.py
    +-- [input]
    ¦   +-- Border_Crossing_Entry_Data.csv
    +-- [output]
    |   +-- report.csv
    +-- [insight_testsuite]
        +-- run_tests.sh
        +-- [tests]
            +-- [test_1]
            |   +-- [input]
            |   ¦   +-- Border_Crossing_Entry_Data.csv
            |   |__ [output]
            |   ¦   +-- report.csv
            +-- [test_2]
                +-- [input]
                ¦   +-- Border_Crossing_Entry_Data.csv
                |-- [output]
                    +-- report.csv


* [src] contains the source files: 'border_analytics.py' and 'functions.py'

* [input] the input file should go here named as 'Border_Crossing_Entry_Data.csv'

* [output] here is where the output file will go: 'report.csv'

* [insight_testsuite]: contains the files to test the program

* [test_1] and [test_2]: are two different tests.


3.- SOURCE CODE:

   There are two files: 'border_analytics.py' and 'functions.py'.

3.1. 'border_analytics.py':
   It calls the required functions to read the input file, process the information, and write 
the output file. 

Because we are working with large ammount of information, efficient use of memory is a priority.
For this reason, 'border_analytics.py' works in two steps. In the first one, it reads one chunck 
of the input csv at a time, processes it and writes it into a temp file. In step two, the temp file
is read and its rows sorted by date, producing the final output file (report.csv).

3.2. 'functions.py':
   It contains the functions needed by 'border_analytics.py':

* create_lists():             Creates two lists, one containing the different Borders and the other
                              one containing the different Measure. This two list will be used to
                              select the chunck from the input file.

* create_transport_matrix():  Takes a chunck from the input file for the given border and mean of 
                              crossing the border (Measure).

* total_crossings():          Calculates the total number of border-crossings for the given chunck.

* running_averages():         Computes the running averages for the given chunck. 

* sort_by_date():             Sorts the temp file by date.


3.3.  Modules:
   This program requires importing the following modules: csv,  decimal,  datetime, os


4.- RUNNING THE PROGRAM:

   Running this program can be done by running 'run.sh'.


5.- TESTING:

   Testing this program can be done by running 'run_tests.sh'. This will run both test in the
folder 'test'. It will create a file in the folder 'insight_testsuite' called 'results.txt'. It
will show if the tests have been passed or not.

An example of tests passed:

[29 Oct 2019 13:49:13] 2 of 2 tests passed

An example of tests not passed:

[29 Oct 2019 13:49:13] 0 of 2 tests passed
