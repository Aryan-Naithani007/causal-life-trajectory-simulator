from src.story import generate_story

import copy
from src.model import LifeState
from src.simulation import simulate_life
from src.analysis import find_fork_month
from src.visualize import plot_futures


base_person = LifeState(
    sleep=4,
    focus=6,
    learning_consistency=5,
    skill_level=20,
    procrastination=6
)

futures = {
    "Conservative": simulate_life(copy.deepcopy(base_person), "conservative"),
    "Aggressive": simulate_life(copy.deepcopy(base_person), "aggressive"),
    "Chaotic": simulate_life(copy.deepcopy(base_person), "chaotic")
}

fork = find_fork_month(futures)
print("⚠️ Life fork point at month:", fork)

plot_futures(futures, fork)

story = generate_story(futures, fork)
print("\n--- STORY MODE ---")
print(story)

