# A - Bottled Up Feelings
# ACM ECNA 2015 Practice Set
# Tejas Deshpande

if __name__ == "__main__":
	
	# input
	input_line = raw_input()
	input_line = input_line.split(" ")
	input_line = map(int, input_line)

	total_volume, big_bottle_volume, small_bottle_volume = input_line

	big_bottle_count = 0
	small_bottle_count = 0

	while(total_volume > 0):
		if (total_volume % big_bottle_volume == 0):
			big_bottle_count = total_volume/big_bottle_volume
			total_volume = 0
		else:
			total_volume -= small_bottle_volume
			small_bottle_count += 1

	if (total_volume < 0):
		print "Impossible"
	else:
		print big_bottle_count, small_bottle_count
