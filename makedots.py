data = open('data.txt').read()

tokens = data.split(" ")

gridsize = 25

y = 0
output = "<svg xmlns='http://www.w3.org/2000/svg' version='1.1'>"
for token in tokens:
    x = 0
    for char in token:
        if char != '1' and char != '0':
            continue
        color = "white"
        if char == '1':
            color = "blue"
        output += "<circle cx='%d' cy='%d' r='7' stroke='black' stroke-width='2' fill='%s' />" % (gridsize * ( 2 + x), gridsize * ( 2 + y), color)
        x += 1
    y += 1

output += "</svg>"


open('/var/www/dots.svg', 'w').write(output)
