from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG


def check_kolatz_hypotize(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(n)
