import streamlit as st
import copy

from src.model import LifeState
from src.simulation import simulate_life
from src.analysis import find_fork_month
from src.story import generate_story
from src.visualize import plot_futures

st.set_page_config(page_title="Causal Life Trajectory Simulator")

st.title("Causal Life Trajectory Simulator")
st.write(
    "This simulator models how small behavioral differences "
    "can compound into very different long-term outcomes."
)
st.caption("Values are normalized and simulated monthly over a 5-year horizon.")
st.sidebar.subheader("Presets")

preset = st.sidebar.selectbox(
    "Choose a preset",
    ["Custom", "Burnout Student", "Disciplined Learner", "Inconsistent Explorer"]
)

if preset == "Burnout Student":
    sleep, focus, learning_consistency, skill_level, procrastination = 3.0, 4.0, 4.0, 15.0, 7.0
elif preset == "Disciplined Learner":
    sleep, focus, learning_consistency, skill_level, procrastination = 7.0, 7.0, 7.0, 20.0, 3.0
elif preset == "Inconsistent Explorer":
    sleep, focus, learning_consistency, skill_level, procrastination = 5.0, 5.0, 4.0, 18.0, 5.0

st.sidebar.header("Initial Life Conditions")

sleep = st.sidebar.slider("Sleep Quality", 0.0, 10.0, 4.0)
focus = st.sidebar.slider("Focus Level", 0.0, 10.0, 6.0)
learning_consistency = st.sidebar.slider("Learning Consistency", 0.0, 10.0, 5.0)
skill_level = st.sidebar.slider("Initial Skill Level", 0.0, 100.0, 20.0)
procrastination = st.sidebar.slider("Procrastination", 0.0, 10.0, 6.0)

if st.sidebar.button("Simulate"):
    base_person = LifeState(
        sleep=sleep,
        focus=focus,
        learning_consistency=learning_consistency,
        skill_level=skill_level,
        procrastination=procrastination
    )

    futures = {
        "Conservative": simulate_life(copy.deepcopy(base_person), "conservative"),
        "Aggressive": simulate_life(copy.deepcopy(base_person), "aggressive"),
        "Chaotic": simulate_life(copy.deepcopy(base_person), "chaotic")
    }

    fork = find_fork_month(futures)

    st.subheader("Simulation Results")
    st.write(f"⚠️ Life fork point detected at month **{fork}**")

    # Plot
    st.pyplot(plot_futures(futures, fork))

    # Story
    st.subheader("Story Mode")
    story = generate_story(futures, fork)
    st.text(story)
