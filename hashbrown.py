import traceback

#border should be {'southwest': 'lat,lng', 'northeast': 'lat,lng', 'geo_piece': 5}
#lat and lng should be sting value like: '-37.841713', '145.00844000000006'
def geohash(border, lat, lng, debug=True):

    try:

	if debug:
	    print border

	geo_piece = border['geo_piece']
        left_bottom = border['southwest'].split(',')
        right_top = border['northeast'].split(',')

        right_top_x = float(right_top[1])
	left_bottom_y = float(left_bottom[0])

        x_length = abs(right_top_x - float(left_bottom[1])) / geo_piece
        y_length = abs(left_bottom_y - float(right_top[0])) / geo_piece

	if debug:
	    print x_length, y_length

        #x,y both from right bottom, from 0 to geo_piece - 1
        x = abs(right_top_x - float(lng)) / x_length
        y = abs(left_bottom_y - float(lat)) / y_length

	if debug:
	    print x, y

	string_x = str(x)
	string_y = str(y)

        return (string_x[:string_x.find('.')], string_y[:string_y.find('.')])

    except:
	if debug:
	    traceback.print_exc(file=config.sys.stdout)
	pass

    return None

#test demo
print geohash({'southwest': '-37.8515778,145.0031555', 'northeast': '-37.8305302,145.0326167', 'geo_piece': 5}, '-37.841713', '145.00844000000006')
