quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

quoteUpper = quote.upper().isupper()

print(quoteUpper)

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

quoteLower = quote.lower()

print(quoteLower)

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

quoteEndsWith = quote.endswith('street')

print(quoteEndsWith)

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

quoteIsUpper = quote.isupper()

print(quoteIsUpper)

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

quoteFind = quote.find('one')

print(quoteFind)

quoteReplace = quote.replace('one', '1')

print(quoteReplace)


quoteReplace2 = quote.replace('one', '1').replace('both', '2')

print(quoteReplace2)

quoteSplit = quote.split(' ')

print(quoteSplit)

print('is digit ? ', quote.isdigit(), ' \nis decimal ? ', quote.isdecimal(), 'is string without numbers?',
      quote.isalpha(), 'is it with string and numbers?', quote.isalnum())
