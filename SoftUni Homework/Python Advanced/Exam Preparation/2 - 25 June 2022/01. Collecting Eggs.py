from collections import deque
eggs = deque(map(int, input().split(', ')))
papers = deque(map(int, input().split(', ')))
boxes_cnt = 0

while eggs and papers:
    egg = eggs.popleft()

    if egg <= 0:
        continue

    elif egg == 13:
        first, last = papers.popleft(), papers.pop()
        papers.append(first)
        papers.appendleft(last)
        continue

    paper = papers.pop()
    if egg + paper <= 50:
        boxes_cnt += 1


if boxes_cnt > 0:
    print(f'Great! You filled {boxes_cnt} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(str(x) for x in eggs)}')

elif papers:
    print(f'Pieces of paper left: {", ".join(str(x) for x in papers)}')
