# agent.py
import random
import config

class Cat:
    def __init__(self,age=0):
        # 個体が生まれたときの初期状態
        self.age = age
        self.is_alive = True
        self.is_pregnant = False
        self.pregnancy_time = 0
        self.can_be_pregnant = False
        self.sterilized = False

    def update(self,N,trap_rate):

        if not self.is_alive:
            return

        p_d = config.P_DEATH
        #p_b = config.P_REPRODUCE
        p_b = config.P_DEATH_K
        K   = config.KCAP

        P_EFF = p_d - ( p_d - p_b ) * N / K

        if random.random() < P_EFF:
            self.is_alive = False

            return

        self.age += 1

        if random.random() < trap_rate:
            self.sterilized = True

        if self.is_alive and self.age >= config.MATURE_AGE and not self.sterilized and not self.is_pregnant:
            self.can_be_pregnant = True

        return

    def reproduce(self):

        if self.can_be_pregnant:
            if random.random() < config.P_PREGNANCY:
                self.is_pregnant = True  
                self.can_be_pregnant = False

        elif self.is_pregnant:
            self.pregnancy_time += 1
            if self.pregnancy_time >= 60:
                newborns = []
                self.is_pregnant = False
                self.pregnancy_time = 0
                for _ in range(config.LITTER_SIZE):
                    newborns.append(Cat())
                return newborns
        return None