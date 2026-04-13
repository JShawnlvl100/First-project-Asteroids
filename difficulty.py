class Difficulty:
    def __init__(self, threshold=2000, speed_step=0.2):
        self.threshold = threshold
        self.speed_step = speed_step
        self.last_level = 0

    def get_level(self, score):
        return score // self.threshold

    def get_multiplier(self, score):
        return 1 + self.get_level(score) * self.speed_step

    def has_increased(self, score):
        level = self.get_level(score)
        if level > self.last_level:
            self.last_level = level
            return True
        return False