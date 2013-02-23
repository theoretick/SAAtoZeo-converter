##Description##
Parses SleepAsAndroid export CSV files into a compatible format with Zeo Sleep Manager.  

A lot of the methods I use for this are pretty horrid and non-pythonic. More of an exercise proof-of-concept. For now, manual parsing and messy, next iteration will use CSV module and dictionaries/tuples.

Currently just deletes Comments, Ratings, Timezone, ID, and Framerate.

##Todo##

- date/time format conversion
- All calculations for ZQ
- hours -> minutes.
