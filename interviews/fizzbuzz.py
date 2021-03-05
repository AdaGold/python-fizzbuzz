def fizzbuzz(number):
    current_number = 1
    answer = []

    for current_number in range(1, number + 1):
        if current_number % 3 == 0:
            answer.append("Fizz")
        elif current_number % 5 == 0:
            answer.append("Buzz")
        elif current_number % 3 == 0 and current_number % 5 == 0:
            answer.append("FizzBuzz")
        else:
            answer.append(f"{current_number}")
    
    return answer
