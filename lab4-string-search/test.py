import random

from string_search import boyer_moore, naive


print("Naïve string search test:")
print("\t Empty arguments test.\t\t\tExpected: []. \t\tFound: ", naive("", ""))
print("\t Equal arguments test. \t\t\tExpected: [0]. \t\tFound: ", naive("123", "123"))
print("\t Text is smaller than String test.\tExpected: []. \t\tFound: ", naive("123", "12"))
print("\t String in Text test.\t\t\tExpected: [2]. \t\tFound: ", naive("123", "3212323"))
print("\t Multiple Strings in Text test. \tExpected: [2, 6]. \tFound: ", naive("123", "3212321233"))
print("\t String in the end of the text test. \tExpected: [6]. \t\tFound: ", naive("123", "121213123"))
print("\t No Strings in Text test. \t\tExpected: []. \t\tFound: ", naive("123", "434343"))


text = ''.join(random.choice(["A", "B", "C"]) for i in range(60))
naive_result = naive("ABA", text)
boyer_moore_result = boyer_moore("ABA", text)

print("Naïve search result: ", "\t\t", naive_result,)
print("Boyer Moore search result: ", "\t", boyer_moore_result)
if naive_result == boyer_moore_result:
    print("Success\n")
print_text = ''
text_index = ''
i = 0
for char in text:
    print_text += char + "  "
    text_index += str(i).ljust(3)
    i += 1
print("Test string with indexes:")
print(print_text)
print(text_index)
