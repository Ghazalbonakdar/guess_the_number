import random
def gen_rand_num(lower_limit, upper_limit) :
    return random.randint(lower_limit, upper_limit)

def main() :
    ll, ul = int(input("lower limit : ")), int(input("upper limit : "))
    choice = gen_rand_num(ll, ul)
    
    while True :
        guess = int(input("Enter your guess: "))
        if choice < guess :
            print("too high")
        elif choice > guess :
            print("too low")
        else :
            print("You Won")
            break
main()