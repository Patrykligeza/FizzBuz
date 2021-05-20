od_j_do_s = [1, 100]
trzy = 3
piec = 5
trzy_i_p = [trzy, piec]
number = od_j_do_s
def FizzBuz(number: int) -> str:
    if number // trzy_i_p:
        print('FizzBuzz')
    if number // 3:
        print("Fizz")
    if number // 5:
        print("Buzz")


for od_j_do_s in od_j_do_s:
    print(FizzBuz())
