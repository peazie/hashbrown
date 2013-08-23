![alt tag](https://raw.github.com/peazie/hashbrown/master/demo.png)

geohash (u know border geo, north west and south east, give any geo inside this border, need calculate which 5x5 area it inside):

input: border geo info, click point geo info, geo piece
output: x section number, y section number

1. init hash, build 2 index from left to right and from top to bottom, how many squares want split

total split number = 5

length of one split size from left to right = (|north west lat -  south east lat|) / total split number 

length of one split size from top to bottom = (|north west lng -  south east lng|) / total split number 

2. calculate, give 1 geo location (lat, lng), 

left position = total split number - ((|lat - north west lat|) % length of one split size from left to right)

top position = total split number - ((|lng - north west lng|) % length of one split size from top to bottom)

3. returne 2 position




draw area border on google map:
https://developers.google.com/maps/documentation/javascript/examples/polygon-simple

