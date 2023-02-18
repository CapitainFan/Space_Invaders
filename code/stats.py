class Stats:
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('code/best_score.txt', 'r') as file:
            self.best_score = int(file.readline())

    def reset_stats(self):
        self.hp_left = 3
        self.score = 0
