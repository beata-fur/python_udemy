article = """ Pierwsza seria „Latającego cyrku” miała pierwotnie dawać główne pole do popisu Cleese’owi, ten chciał jednak współpracować z innymi. Tak oto powstała zorganizowana grupa, dla której utworzono rutynowe zasady działania. Każdy dzień pisania rozpoczynał się o 9:00 rano i trwał do 17:00. Na początku typowego tygodnia pracy Cleese i Chapman pisali w odosobnieniu jako jedna spółka autorska, Jones i Palin jako druga, a Idle pisał sam. Po kilku dniach cała grupa spotykała się wraz z Gilliamem i krytykowała nawzajem swoje scenariusze oraz wymieniała poglądy. Podchodzili do pisania demokratycznie. Jeśli coś rozśmieszyło większość, zatwierdzano to jako część programu. W podobny sposób obsadzano role – nie było problemów z egocentryzmem, gdyż każdy z Pythonów czuł się bardziej autorem niż aktorem. Po dobraniu i uporządkowaniu kolejności skeczy do danego odcinka, Gilliam miał wolną rękę w łączeniu ich w całość za pomocą wymyślnych animacji, uzbrojony w kamerę, nożyczki i farbę.

Zanim wymyślono nazwę „Latający cyrk Monty Pythona”, powstało kilka innych tytułów roboczych, m.in. Owl Stretching Time (Pora rozciągania sów), Bunn, Wacket, Buzzard, Stubble and Boot, Gwen Dibley's Flying Circus (Latający Cyrk Gwen Dibley).

Zespół miał bardzo konkretny pomysł na serial i był bardzo zawiedziony, gdy Spike Milligan nagrał swój program komediowy Q5 w nieco podobnym duchu. Pythoni przyznawali się do inspiracji Milliganem, lecz styl „Latającego cyrku” jest zdecydowanie inny. Wyróżniają go szczególnie niepowtarzalne animacje Gilliama, ale także proces wzajemnej krytyki i selekcji materiału."""

articleUpper = article.upper()

print(articleUpper)

articleLower = article.lower().replace('monty', 'flying')

print(articleLower)

print(article.split(' '))

print('slowo pythona wystepuje', article.count('Pythona'), 'raz/razy')

print("to print the \ you need to put \ twice in your text like this: \\\\")

print('The best hits of \'80s!!!')

print("The best hits of '80s!!! ")


amountPLN = 234
a = 3.65
b = 4.23

print('cur,  exchange,   amount')
print('USD, ', a, amountPLN/a, sep='    ')
print('EUR, ', b, amountPLN/b, sep='    ')

ValueAsText = '123.45'
factor = 1.23

print('value is', ValueAsText, 'factor is', factor, 'value*factor= ', float(ValueAsText)*factor)

