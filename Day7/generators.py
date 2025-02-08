# import time
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count  # Yield returns the value and suspends the function
#         count += 1
# counter = count_up_to(10000)

# # Use a loop to get values one at a time
# for number in counter:
#     time.sleep(10)
#     print(number)
import time
def generate_a_sublist(max):
    count = 0
    max_range = 100
    while count < max:
        # Generate a sublist of 100 numbers starting from `count` to `count + 100`
        new_list = [x for x in range(count, min(count + 100, max)) if x % 100 == 0]
        yield len(new_list)
        count += 100  # Move the starting point by 100 for the next iteration

# Example usage
alist = generate_a_sublist(100000000)
for a_list in alist:
    #time.sleep(10)
    print(a_list)


#Same Function without a generator
def generate_a_list(max):
    # Generate a list with numbers from 0 to `max` that are divisible by 1,000,000
    new_list = [x for x in range(max) if x % 100 == 0]
    return len(new_list)

print(generate_a_list(100000000))