def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) <= 3:
        scores.sort(reverse=True)
        return scores
    else:
        ret = []
        for i in range(3):
            top_score = max(scores)
            ret.append(top_score)
            scores.remove(top_score)
        return ret