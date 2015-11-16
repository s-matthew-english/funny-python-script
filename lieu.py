f = open('./data.txt', 'r')
array = []
for line in f:
    number = int(line.split(':')[1])
    array.append(number)
print( 'echo "' + str( sum(array) ) + '.0" | xclip -selection c' )
