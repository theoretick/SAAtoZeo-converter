##Description##
Parses SleepAsAndroid export CSV files into a compatible format with Zeo Sleep Manager.  

A lot of the methods I use for this are pretty horrid and non-pythonic. More of an exercise proof-of-concept. For now, manual parsing and messy, next iteration will use CSV module and dictionaries/tuples.

##Function##

    user$ python saa-to-zeo.py sleepasandroid-export.csv
    "Done. exported to zeostyle-export.csv"

- Reorders columns
- (Currently just) deletes Comments, Ratings, Timezone, ID, and Framerate.
- Retitles columns
- Changes hours to minutes

##Todo##

- add zeo excess columns (wake-time, deep time) to populate later
- date/time format conversion
- figure out how to calc and add all calculations for ZQ
