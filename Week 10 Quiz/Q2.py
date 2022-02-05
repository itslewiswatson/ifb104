new = open('outfile.txt', 'w')
old = open('infile.txt', 'r')

for line in old:
    new.write(line)
    new.write('\n')

new.close()
old.close()