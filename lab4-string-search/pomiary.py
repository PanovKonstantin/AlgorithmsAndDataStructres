import timeit

from string_search import boyer_moore, naive


def naive_test():
    for word in words[:n]:
        naive(word, text)


def boyer_moore_test():
    for word in words[:n]:
        boyer_moore(word, text)


f = open("pan-tadeusz.txt", encoding="utf-8")
text = f.read()
words = text.split()
print('{:>36s}'.format("Naïve search"), '{:>37s}'.format("Boyer Moore search"))
for n in range(100, 1001, 100):
    print('{:>20s}'.format(f"Time for {n} elements:"), end="\t")
    print('{:<30s}'.format(str(timeit.timeit(naive_test, number=1))), end="\t")
    print('{:<30s}'.format(str(timeit.timeit(naive_test, number=1))))
