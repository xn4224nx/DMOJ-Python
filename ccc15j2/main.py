"""
https://dmoj.ca/problem/ccc15j2
"""


def message_sentiment():
    """
    How happy or sad is the message.
    """
    msg = input()

    happy_cnt = msg.count(":-)")
    sad_cnt = msg.count(":-(")

    if happy_cnt == 0 and sad_cnt == 0:
        print("none")
    elif happy_cnt < sad_cnt:
        print("sad")
    elif happy_cnt > sad_cnt:
        print("happy")
    else:
        print("unsure")


if __name__ == "__main__":
    message_sentiment()
