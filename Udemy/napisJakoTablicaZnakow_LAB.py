q = "THE EYES"

print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])

print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])

p = "a gentleman"

print(p)
print(p[3], p[6], p[7], p[2], p[0], p[4], p[5], p[1], p[8:])
print(p[3] + p[6] + p[7] + p[2] + p[0] + p[4] + p[5] + p[1] + p[8:])

r = "THE MORSE CODE"
#here come dots

print(r)
print(r[1:3]+r[6]+r[8], r[10:12]+r[4]+r[2], r[11:13][::-1]+r[0]+r[7])

x = "dupa"
print(x[0:2])
print(x[0:2][::-1])


line = 'Dzisiaj nadamy o: 06:00 Program "Pytanie na śniadanie"'

timeStartIndex = line.find(":")
timeStopIndex = timeStartIndex + 7


print(timeStartIndex)
print(timeStopIndex)

time = line[timeStartIndex:timeStopIndex]
print("Time: " + time)

tmpStartIndex = line.find('"')

print(tmpStartIndex)

print(line[tmpStartIndex + 1:])

tmp = line[tmpStartIndex + 1:]

tmpEndIndex = tmp.find('"')

print(tmpEndIndex)

title = tmp[0:tmpEndIndex]

print("Title: " + title)


