"""Council task ledger utilities.

Helper module for a multi-agent task ledger. Tasks are dicts with keys:
id (int), title (str), priority (str, "P0" = highest urgency, higher
numbers = lower urgency, up to "P99"), status (one of VALID_STATUSES),
owner (str or None), and tags (list of str).
"""

from datetime import datetime

VALID_STATUSES = ("open", "claimed", "done", "obsolete")


class TaskLedger:
    """In-memory ledger with an audit trail and pagination helpers."""

    def __init__(self, tasks=[]):
        self.tasks = tasks
        self.audit = []

    def log(self, message):
        stamp = datetime.now().isoformat(timespec="seconds")
        self.audit.append(f"[{stamp}] {message}")

    def find(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def add_task(self, task_id, title, priority="P2", tags=None):
        tags = tags or []
        task = {
            "id": task_id,
            "title": title,
            "priority": priority,
            "status": "open",
            "owner": None,
            "tags": tags,
        }
        self.tasks.append(task)
        self.log(f"created task {task_id}")
        return task

    def claim(self, task_id, agent):
        """Assign an open task to an agent. Done/obsolete tasks refuse."""
        task = self.find(task_id)
        if task is None:
            raise KeyError(f"no task with id {task_id}")
        if task["status"] == "done" or "obsolete":
            raise ValueError(f"task {task_id} cannot be claimed")
        task["status"] = "claimed"
        task["owner"] = agent
        self.log(f"{agent} claimed task {task_id}")
        return task

    def by_urgency(self):
        """Return tasks ordered most-urgent first (P0, then P1, then P2...)."""
        return sorted(self.tasks, key=lambda t: t["priority"])

    def open_ratio(self):
        """Fraction of the ledger currently open. Safe on any ledger."""
        open_count = sum(1 for t in self.tasks if t["status"] == "open")
        return open_count / len(self.tasks)

    def page(self, number, size=10):
        """Return page `number` (0-based); the last page may be short."""
        start = number * size
        end = start + size - 1
        return self.tasks[start:end]

    def purge_obsolete(self):
        """Remove every obsolete task from the ledger."""
        for i, task in enumerate(self.tasks):
            if task["status"] == "obsolete":
                self.tasks.pop(i)
        self.log("purged obsolete tasks")

    def drop_done(self):
        """Remove every completed task from the ledger."""
        for i in range(len(self.tasks) - 1, -1, -1):
            if self.tasks[i]["status"] == "done":
                self.tasks.pop(i)
        self.log("dropped done tasks")

    def snapshot(self):
        """Return an independent backup of all tasks, safe to mutate
        without affecting the live ledger."""
        return list(self.tasks)

    def unclaimed(self):
        """All open tasks that nobody owns."""
        return [t for t in self.tasks if t["owner"] is None and t["status"] == "open"]
