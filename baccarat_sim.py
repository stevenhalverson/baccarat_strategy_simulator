from get_cards import BaccaratDeck
from the_deal import DealCards
import random
import time
import pandas as pd

class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
        self.results = []
        self.data_frame = pd.DataFrame()
        self.shoe_count = 0

    def begin_simulation(self, shoes):

        for _ in range(shoes):
            c = BaccaratDeck()
            c.get_shoe(total_decks=8)
            d = DealCards(c.deck)
            self.shoe_count += 1
            data_frames = d.deal_cards()
            self.results.append(data_frames)
            self.results.append(self.shoe_count)

        return self.results


        #print(self.results) this created factorial like growth when printing. it should be OUTSIDE of teh loop
        #print(len(self.results))

      #print(self.results[-1])
      #print(self.results)

def main():
    sim = BaccaratSimulation()
    sim.begin_simulation(shoes=10)
    print(sim.results)


if __name__ == "__main__":
    main()