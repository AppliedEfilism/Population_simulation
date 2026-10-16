# main.py  
import matplotlib.pyplot as plt
import config
import random
from agent import Cat

ls = ["-", "--", "-."]
trap_rates = [0.0, 2e-3, 5e-3]

def main():

    for i, trap_rate in enumerate(trap_rates):

        annual_trap_rate = 1-(1-trap_rate)**365

        cats = []
        for _ in range(config.N0):
            age = int(300*random.random())
            cats.append(Cat(age))

        N_history = []

        for step in range(config.NSTEP):
            N_current = len(cats)
            N_history.append(N_current)

            new_cats = [] 

            day_of_year = ( step % 365 ) + 1

            for cat in cats:

                cat.update(N_current,trap_rate)

                if day_of_year <= config.BREEDING_SEASON_LENGTH:

                    offspring = cat.reproduce()
                    if offspring is not None:
                        #new_cats.append(offspring)
                        new_cats.extend(offspring)

            cats = [cat for cat in cats if cat.is_alive]
            cats.extend(new_cats)

        plt.plot(N_history, label=f"trap rate={trap_rate:.3f} (annual rate={annual_trap_rate:.2f})", ls=ls[i])
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.ylim(0,200)
    plt.grid(True, alpha=0.5)
    plt.legend(loc="upper right")
    plt.savefig(f"fig_ABM_cat.png")
    plt.show()

if __name__ == "__main__":
    main()