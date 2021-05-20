
def FizzBuz(number: int) -> str:
    if number % [3, 5]:
        print('FizzBuzz')
    if number % 3:
        print("Fizz")
    if number % 5:
        print("Buzz")


for number in range[1, 100]:
    print(FizzBuz())
