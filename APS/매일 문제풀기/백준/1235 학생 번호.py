def student_number(numbers):
    answer = 0
    for idx in range(1, len(numbers[0]) + 1):
        temp = [num[:idx] for num in numbers]

        if len(temp) == len(set(temp)):
            answer = idx
            break

    return answer


if __name__ == "__main__":
    numbers = []

    for _ in range(int(input())):
        number = input()
        numbers.append(number[::-1])

    print(student_number(numbers))
