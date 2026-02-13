import matplotlib.pyplot as plt


def plot_futures(futures, fork):
    plt.figure()

    for name, result in futures.items():
        months = [p["month"] for p in result]
        skills = [p["skill"] for p in result]
        focus = [p["focus"] for p in result]

        plt.plot(months, skills, label=name)

        burnout_months = [months[i] for i in range(len(focus)) if focus[i] == 0]
        burnout_skills = [skills[i] for i in range(len(focus)) if focus[i] == 0]
        plt.scatter(burnout_months, burnout_skills)

    plt.axvline(x=fork, linestyle="--")
    plt.text(fork + 0.5, plt.ylim()[1] * 0.9, "Life Fork Point", rotation=90)

    plt.xlabel("Time (Months)")
    plt.ylabel("Skill Level")
    plt.title("Causal Life Trajectory Simulator")
    plt.legend()
    plt.grid(True)
    return plt
