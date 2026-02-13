class LifeState:
    def __init__(self, sleep, focus, learning_consistency, skill_level, procrastination):
        self.sleep = sleep
        self.focus = focus
        self.learning_consistency = learning_consistency
        self.skill_level = skill_level
        self.procrastination = procrastination


def clamp(value, min_val=0, max_val=10):
    return max(min(value, max_val), min_val)
