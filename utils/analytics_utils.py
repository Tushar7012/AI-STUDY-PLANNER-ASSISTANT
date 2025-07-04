from typing import Dict

def compute_progress(subject_topics: Dict[str, list], completed: Dict[str, list]) -> Dict[str, float]:
    stats = {}
    for subject, topics in subject_topics.items():
        total = len(topics)
        done = len(completed.get(subject, []))
        stats[subject] = round(done / total * 100, 1) if total > 0 else 0.0
    return stats

def summary_stats(analytics: Dict[str, float]) -> str:
    lines = [f"{sub}: {pct}% complete" for sub, pct in analytics.items()]
    return "\n".join(lines)
