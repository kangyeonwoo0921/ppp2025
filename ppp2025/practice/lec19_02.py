import numpy as np
import matplotlib.pyplot as plt

def main():
    dices = np.random.randint(1, 7, size = 100)
    print(dices)
    
    fig, ax = plt.subplots()
    
    ax.hist(dices, bins = 6, color ="b")
    plt.show()

if __name__=="__main__":
    main()