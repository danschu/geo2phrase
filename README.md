#  GeoPhrase Generator
The GeoPhrase Generator is a Python program that converts geographic coordinates (longitude and latitude) into memorable phrases, making it easier to recall specific locations. This tool utilizes a customizable wordlist sourced from [MarvinJWendt's Gist](https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4) to create unique and engaging phrases from raw coordinate values. Importantly, any wordlist from any language can be used, allowing for broad applicability across different linguistic contexts.

## Exmaplae:

Convert the coordinates of the Eiffel-tower to phrase and back againg with an accuracy of 3.7cm x 1.9cm
```py
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
```

Output 

```cmd
Input coords [lat: 48.8583736, lon: 2.2919064]
Phrase: Ausgabenbeleg.abzukneifen.Ansammelns.alliierendes
Reconstructed coords [lat: 48.85837367735803, lon: 2.2919065319001675]
```  

You can change the wordlist, add new words and remove existing ones. The conversion from the phrase back to the coords will still work! If you remove the word 'Ansammelns' from the wordlist, it is replaced by a word with the same hash:

```cmd
Input coords [lat: 48.8583736, lon: 2.2919064]
Phrase: ausgelüftetem.abzukneifen.basisnäheren.alliierendes
Reconstructed coords [lat: 48.85837367735803, lon: 2.2919065319001675]
```

The meaning if the words are not important, both of the follwing phrases result in the same coodinate. This is also the reason you can use differnt language py simply swapping out the wordlist.

```
    ausgelüftetem.abzukneifen.basisnäheren.alliierendes
    Ausgabenbeleg.abzukneifen.Ansammelns.alliierendes
``` 


## How It Works
1) Initialization: The program initializes a wordlist from a specified text file (wordlist-german.txt). It filters out long words and creates a lookup table that maps geohash values to words. You can replace this file with any wordlist in any language to customize the phrases generated.
2) Geographic to Phrase Conversion: The geo2phrase function takes longitude and latitude as input, encodes them into a geohash, and then converts the geohash into a sequence of words based on the lookup table.
3) Phrase to Geographic Conversion: The phrase2geo function takes a phrase (a sequence of words) and decodes it back into geographic coordinates. It uses the hash of each word to find the corresponding geohash characters.
Key Features


## Key Features
1) Customizable Wordlist: Users can utilize any wordlist from any language, allowing for broad applicability and personalization of generated phrases.
Hash-Indexed Words: The words in the wordlist are hashed and indexed, ensuring that the system remains functional even if words are added or removed from the list.
2) Adjustable Accuracy: Users can modify the precision of the generated phrases, affecting the number of words used to represent a location. For example, higher precision results in more words, while lower precision results in fewer words.
3) Efficient Encoding and Decoding: The system can convert phrases back into coordinates without requiring the original wordlist, using the hash of the words in the generated phrases for efficient decoding.
4) Flexible Location Representation: The program allows for varying levels of accuracy, enabling users to choose how detailed or concise they want the location representation to be.
5) Alternative to Existing Systems: The GeoPhrase Generator serves as a unique alternative to other location encoding systems such as What3words, Mapcode, Geohash, and Fixphrase, offering a different approach to geographic data representation