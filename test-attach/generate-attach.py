def generate(size):
    f = open("test-{}{}.txt".format(size, "MB"), "a")
    for i in range(0, size*1024*1024):
        f.write("a")
    f.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("1 argument passed")
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print("Usage: ...")
        else:
            generate(int(sys.argv[1]))