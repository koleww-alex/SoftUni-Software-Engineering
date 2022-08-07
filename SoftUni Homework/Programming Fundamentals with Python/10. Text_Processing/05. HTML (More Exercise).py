def title_func(words: list):
    print("<h1>")
    print(f"    {' '.join(words)}")
    print("</h1>")


def article_func(words: list):
    print("<article>")
    print(f"    {' '.join(words)}")
    print("</article>")


def content_func(words: list):
    print("<div>")
    print(f"    {' '.join(words)}")
    print("</div>")


title = input().split()
article = input().split()

title_func(title)
article_func(article)

while True:
    comment = input()
    if "end of comments" in comment:
        break
    comment = comment.split()
    content_func(comment)
