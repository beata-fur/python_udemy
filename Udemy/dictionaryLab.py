chanels = {'Google': '1480', 'Email': '300', 'Natural Graffic': '440', 'TV Spot': '700'}

print(chanels.get('Email'))

chanelsUpdate = {'Natural Traffic': '520', 'News': '600'}

chanels.update(chanelsUpdate)

print(chanels)
print(chanels.keys())
chanels.pop('Email')
print(chanels)


