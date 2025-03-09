"""

  Example program for converting lon/lat values into phrases (words)
  the wordlist is used from https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4
  
  It uses geohash to convert the coordinate into a string and then
  splits the string into chunks of three chars, which are converted to a word.
  
  The words are hashed-indexed (if you remove or add new words to the wordlist, it still works with old phrases)
  
  You can change the accuracy, which results into more or less words needed:
    4.8m x 4.8m -> 3 words
    3.7cm x 1.9cm -> 4 words
  
    
  Alternative to What3words, Mapcode, Geohash, Fixphrase etc.
  
"""

from geohash_phrase import geo2phrase, phrase2geo

    
def main():
    lat, lon = (48.8583736,2.2919064) # Eiffel tower
    """
    Accuracy
    
    1   5,009.4km x 4,992.6km
    2   1,252.3km x 624.1km
    3   156.5km x 156km
    4   39.1km x 19.5km
    5   4.9km x 4.9km
    6   1.2km x 609.4m
    7   152.9m x 152.4m
    8   38.2m x 19m
    9   4.8m x 4.8m
    10  1.2m x 59.5cm
    11  14.9cm x 14.9cm
    12  3.7cm x 1.9cm 
    """

    print(f"Input coords [lat: {lat}, lon: {lon}]")
    phrase = geo2phrase(lat, lon, 12) # Accuracy: 3.7cm x 1.9cm
    print(f"Phrase: {phrase}")
    lat_new, lon_new = phrase2geo(phrase)
    print(f"Reconstructed coords [lat: {lat_new}, lon: {lon_new}]")
    
if __name__ == "__main__":
    main()