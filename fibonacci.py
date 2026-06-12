def generate_fibonacci(n):
    sequence = [0, 1]
    if n == 1:
        return [0]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    try:
        terms = int(input("How many terms? (Max 50): "))
        if 0 < terms <= 50:
            print(generate_fibonacci(terms))
        else:
            print("Please enter a number between 1 and 50.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()