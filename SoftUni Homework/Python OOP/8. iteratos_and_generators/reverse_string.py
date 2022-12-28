def reverse_text(text: str):

    for i in range(len(text) - 1, -1, -1):

        yield text[i]
