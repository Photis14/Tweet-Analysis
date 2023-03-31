# Tweet-Analysis

This program takes a pickled Pandas dataframe of tweets posted by select Suffolk university students from 2020-01-01 to 2020-07-31 and finds the twenty most frequently used hashtags and hashtag-like words for each month. Hashtag-like words are words that equal one of the hashtags, less the # sign. The program counts the hashtags and the matching hashtag-like words together and performs case-insensitive counting.

# Requirements
Python 3.x
Pandas
Pickle
CSV

# How to Run
The name of the input file should be passed to the program as the first command-line argument. The name of the output file will be the same as the name of the input file, except that the extension will be .csv. For example, for the input suffolk.p, the program will produce suffolk.csv.

#Output
The output of the program is a CSV file. The first row of the file contains month names or numbers. The remaining twenty rows contain the most frequently used hashtags, in the order of decreasing use frequency, with the most frequently used hashtag at the top.

# Notes
The program assumes that the input file contains a pickled Pandas dataframe with the following columns: author, id, created_at, full_text, and hashtags.
The program performs case-insensitive counting.
Hashtag-like words are words that equal one of the hashtags, less the # sign (e.g., for the hashtag #rams, rams is a hashtag-like word).
The program may take some time to run, depending on the size of the input file.
