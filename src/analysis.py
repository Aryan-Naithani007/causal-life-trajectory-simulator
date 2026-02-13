def find_fork_month(futures):
    max_gap = 0
    fork_month = 0

    for i in range(len(next(iter(futures.values())))):
        skills = [futures[name][i]["skill"] for name in futures]
        gap = max(skills) - min(skills)

        if gap > max_gap:
            max_gap = gap
            fork_month = i

    return fork_month
