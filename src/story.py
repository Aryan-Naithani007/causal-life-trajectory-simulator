def generate_story(futures, fork):
    lines = []
    lines.append(f"Life fork point detected at month {fork}.")

    for name, result in futures.items():
        focus_values = [p["focus"] for p in result]
        skill_values = [p["skill"] for p in result]

        burnout_months = [i for i, f in enumerate(focus_values) if f == 0]

        if burnout_months:
            lines.append(
                f"{name} path experienced burnout starting at month {burnout_months[0]}."
            )
        else:
            lines.append(
                f"{name} path avoided burnout and maintained stability."
            )

        final_skill = skill_values[-1]
        lines.append(
            f"{name} path ended with skill level {round(final_skill, 1)}."
        )

    return "\n".join(lines)
