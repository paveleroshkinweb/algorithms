from evaluator import evaluate


def main():
    while True:
        expression = input()
        result = evaluate(expression)
        print(result)


if __name__ == '__main__':
    main()