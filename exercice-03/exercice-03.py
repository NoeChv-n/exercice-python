
temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

#1

print(f"Moyenne : {sum(temperatures) / len(temperatures):.2f}")
print(f"Min : {min(temperatures)}")
print(f"Max : {max(temperatures)}")

#2

journee_chaude = 0

for temperature in temperatures :
    if temperature > 15 :
        journee_chaude += 1
print(f"Jour > 15°C : {journee_chaude}")

#3

fahrenheit = []

for temperature in temperatures :
    fahrenheit.append(temperature * 9/5 + 32)

print(f"Températures en Fahrenheit : {fahrenheit}")

#4

for i, temperature in enumerate(temperatures) :
    print(f"Jour {i+1} : {temperature}°C")

