def check_lenght(ticket: str):
    if len(ticket) == 20:
        return True
    return False


def is_valid(ticket: str):
    if check_lenght(ticket):
        symbols = ['@', '#', '$', '^']
        left_part = ticket[:10]
        right_part = ticket[10:]
        for symbol in symbols:
            for repetition in range(10, 5, -1):
                combination = repetition * symbol
                if combination in left_part and combination in right_part and len(combination) == 10:
                    return f'ticket "{ticket}" - {len(combination)}{symbol} Jackpot!'
                elif combination in left_part and combination in right_part:
                    return f'ticket "{ticket}" - {len(combination)}{symbol}'
        return f'ticket "{ticket}" - no match'
    return "invalid ticket"


tickets = [ticket.strip() for ticket in input().split(",")]
for ticket in tickets:
    print(is_valid(ticket))
