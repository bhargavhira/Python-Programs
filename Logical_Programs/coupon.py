import random

def random_number_generator():
    return random.randint(0, 999)

def generate_distinct_coupons(n):
    coupon_set = set()
    counter = 0
    
    while len(coupon_set) < n:
        random_number = random_number_generator()
        counter += 1
        coupon_set.add(random_number)
    
    return counter

def main():
    n = int(input("Enter number of distinct coupons: "))
    total_random_numbers = generate_distinct_coupons(n)
    print(f"Total random numbers needed to generate {n} distinct coupons: {total_random_numbers}")

if __name__ == "__main__":
    main()