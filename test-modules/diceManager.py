# Dice Manager module

# $ python diceManager.roll(n, m)
def roll(diceFaces, diceNumber):
    import random
    results=[]
    for n in range(0, diceNumber):
        result = random.randint(1, diceFaces)
        results.append(result)
    
    return results

# $ python diceManager.py <arg1> <arg2>
# arg1, arg2: int
if __name__ == "__main__":
    import sys
    #print("Parameters: " + str(sys.argv))

    if len(sys.argv) == 1:
        print("Dice Manager module, type help as argument")
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print("Usage: $ python diceManager.py <arg1> <arg2>")
        else:
            results = roll(int(sys.argv[1]), int(sys.argv[2]))
            print(results)