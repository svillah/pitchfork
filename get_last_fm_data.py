#
# This file is to process pitchfork data for use with the Last.fm API
#

import pandas as p

# figure out API stuff and
def get_listens():
    # get listens

def get_tags():
    # get tags


# read in the artist name and album name
pitchfork_data = p.read_csv('output.csv', usecols=['artist', 'album'])

# check that the csv was read in correctly
# print(pitchfork_data.head(5))


# iterate through each record to make lastfm API calls
for row in pitchfork_data.itertuples(index=True, name='Pandas'):

    # testing to check iterating through each record
    print "Artist: ", getattr(row, 'artist'), "Album: ", getattr(row, 'album')

    # make API calls based on artist and album here
    # process response
    # save as a csv

