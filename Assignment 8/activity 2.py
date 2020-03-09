def main():
    while True:
        numbertests = int(input("How many students took the test:"))
        count = 0
        total = 0
        while count < numbertests:
            score = int(input("Enter their score:"))
            total = total + score
            count = count + 1
        print("The average test score is.. ", total / numbertests)
main()
