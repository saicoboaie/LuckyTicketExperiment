import random


def generate_random_ticket():
    ticket = []
    for i in range(0, 6):
        ticket.append(random.randint(0, 9))
    return ticket


def is_lucky(v):
    if int(v[0]) + int(v[1]) + int(v[2]) == int(v[3]) + int(v[4]) + int(v[5]):
        return True
    else:
        return False


def probability_luck():
    lucky_tickets_count = 0
    test_cases_count = 1000000

    for i in range(0, test_cases_count):
        ticket = generate_random_ticket()
        if is_lucky(ticket):
            lucky_tickets_count = lucky_tickets_count + 1

    return lucky_tickets_count / test_cases_count


print(f"Probability of lucky ticket is {probability_luck()}")


