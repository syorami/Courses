# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, str(i + 1)))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0: return i + 1
            if_match = are_matching(opening_brackets_stack[-1].char, next)
            opening_brackets_stack.pop()
            if not if_match: return i + 1

    return 'Success' if len(opening_brackets_stack) == 0 else opening_brackets_stack[-1].position


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
