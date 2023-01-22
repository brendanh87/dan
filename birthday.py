import random

def main():
    d = {}
    with open("birthday.txt") as f:
        for line in f:
            (key, val) = line.split("~")
            d[key] = val

    thing, blurb = random.choice(list(d.items()))

    print(thing)
    print(blurb)
  
if __name__ == '__main__':
    main()