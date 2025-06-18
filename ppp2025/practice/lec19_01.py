import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib 


def main():
    tmax =np.random.rand(30) * 15 +15
    tmin =tmax - (np.random.rand(30) * 5 +5)
    print(tmax)
    print(tmin)
    
    fig, ax = plt.subplots(1, 2)
    ax[1].set_ylim([0, 15])    
    
    ax.plot(tmax, color = "r", label = "TMAX")
    ax.plot(tmin, color = "b", label = "TMIN")
    ax.set_ylabel("온도")
    ax.set_label("DAY")
    


    plt.show()
   
    # plt.savefig("line_graph")
    
    
if __name__=="__main__":
    main()