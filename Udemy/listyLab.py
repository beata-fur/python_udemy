hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN',
              'RIDERS ON THE STORM', 'WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')

print(hitsTitles)

hitsTitles.insert(2, 'HOTEL CALIFORNIA')
print(hitsTitles)
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles)
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
print(hitsTitles)
hitsTitles[0] = 'ENJOY OF SILENCE'
print(hitsTitles)

hitsToRead = hitsTitles.copy()
print(hitsToRead)

hitsToRead.reverse()
print(hitsToRead)
hitsToRead.sort()
print(hitsToRead)
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))

additionalSongs = ['NOTHING COMPARE 2 U', 'WISH YOU WERE HERE']
print(additionalSongs)
hitsToRead.extend(additionalSongs)

print(hitsToRead)


print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsTitles.count('RIDERS ON THE STORM'))

hitsToRead.clear()
print(hitsToRead)





