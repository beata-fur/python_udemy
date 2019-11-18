isAutomaticMode = False
# pokretlo w trybie automatycznym
is80PercentLight = True
# true gdy jest dość widno
isDirectLight = False
# true gry slonce wpada w oczy
isRainy = True
# true gdy pada deszcz

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
# wynik

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)


