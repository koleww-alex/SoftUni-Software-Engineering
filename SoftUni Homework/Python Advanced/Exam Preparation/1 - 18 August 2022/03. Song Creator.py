def add_songs(*args):
    songs = {}
    output = []
    for title, lyrics in args:
        if title not in songs:
            songs[title] = []
        songs[title].extend(lyrics)

    for key, value in songs.items():
        output.append(f'- {key}')
        if value:
            output.append('\n'.join(value))

    return '\n'.join(output)
