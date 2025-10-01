#loops can exist within other loops.
# say you wanted to count to 10 five times


times = 5
outer = 0
while outer < times:

    outer += 1
    print(outer)
    inner = 0
    while inner < outer:
        inner += 1
        print(".    ", inner)
