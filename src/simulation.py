import random
from src.model import clamp, LifeState


def apply_sleep_rule(state):
    if state.sleep < 5:
        state.focus -= 2
        state.learning_consistency -= 1
        state.procrastination += 1


def chaos_event(state):
    chance = random.random()
    if chance < 0.1:
        state.focus -= 1
        state.procrastination += 1
    elif chance > 0.9:
        state.focus += 1
        state.learning_consistency += 1


def apply_personality(state, personality):
    if personality == "conservative":
        state.focus += 0.2
        state.procrastination -= 0.2
    elif personality == "aggressive":
        state.learning_consistency += 0.5
        state.sleep -= 0.3
    elif personality == "chaotic":
        state.focus += random.uniform(-1, 1)


def adaptive_sleep(state, personality):
    if personality == "conservative" and state.focus < 3:
        state.sleep += 0.3
    elif personality == "aggressive" and state.focus < 2:
        state.sleep += 0.1
    elif personality == "chaotic":
        state.sleep += random.uniform(-0.2, 0.4)


def update_skill(state):
    effective_learning = state.learning_consistency * (state.focus / 10)
    growth = effective_learning * 0.6
    penalty = state.procrastination * 0.3
    state.skill_level += max(growth - penalty, 0)


def simulate_life(initial_state, personality, months=60):
    state = initial_state
    history = []

    for month in range(months):
        apply_personality(state, personality)
        adaptive_sleep(state, personality)
        state.sleep = clamp(state.sleep)

        apply_sleep_rule(state)
        chaos_event(state)

        state.focus = clamp(state.focus)
        state.learning_consistency = clamp(state.learning_consistency)
        state.procrastination = clamp(state.procrastination)

        update_skill(state)

        history.append({
            "month": month,
            "skill": round(state.skill_level, 2),
            "focus": round(state.focus, 2)
        })

    return history
