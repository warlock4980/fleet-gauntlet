The Python module `gauntlet_target.py` contains several defects and shared-[7D[K
shared-state hazards. The module is well-documented with clear intent and p[1D[K
purpose.

1. In the `TaskLedger` class, the `by_urgency` method returns tasks in the [K
wrong order. The urgency of the task is determined by the `priority` attrib[6D[K
attribute, and it should be sorted in descending order.

2. In the `claim` method, if the task is already claimed or done, it will n[1D[K
not allow the agent to claim it again.

3. The `open_ratio` method returns an incorrect value. It should return the[3D[K
the fraction of tasks currently in the ledger that are open.

4. The `purge_obsolete` and `drop_done` methods do not remove tasks that ar[2D[K
are obsolete from the ledger, which could leave behind incomplete tasks in [K
the ledger.

5. The `snapshot` method is not used properly. It returns a copy of the led[3D[K
ledger's tasks, but it should return a new list of tasks, not modify the or[2D[K
original.

6. The `unclaimed` method returns tasks that are not assigned to anyone yet[3D[K
yet. However, it does not handle the scenario where an agent claims a task [K
that is unclaimed.

To fix these defects, you need to:

1. Change the `by_urgency` method to sort tasks in descending order of thei[4D[K
their urgency.
2. Fix the `claim` method to handle situations where the task is already cl[2D[K
claimed or done.
3. Improve the `open_ratio` method to accurately represent the fraction of [K
tasks currently in the ledger that are open.
4. Ensure that the `purge_obsolete` and `drop_done` methods do not remove t[1D[K
tasks that are obsolete from the ledger.
5. Improve the `snapshot` method to return a new list of tasks, not the sam[3D[K
same list as the original.
6. Make sure that the `unclaimed` method correctly handles the scenario whe[3D[K
where an agent claims a task that is unclaimed.


