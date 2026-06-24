"""Week 5 — Blocks & Graphs.

Lab: model a block workflow as a directed graph, validate it, and compute a valid execution
order (topological sort).

A *block* is a visible operation with input/output ports and configuration. A *connection*
(edge) sends data from one block's output to another block's input. Before a workflow can run
we must: validate the blocks/edges, detect cycles, and order blocks so each runs after its
dependencies.

Run:
    python graph_validation.py
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class Block:
    """A node in the workflow graph."""

    id: str
    label: str
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    config: Dict[str, object] = field(default_factory=dict)


# A connection links (from_block, from_port) -> (to_block, to_port).
Connection = Tuple[Tuple[str, str], Tuple[str, str]]


class WorkflowGraph:
    def __init__(self, blocks: List[Block], connections: List[Connection]):
        self.blocks: Dict[str, Block] = {b.id: b for b in blocks}
        self.connections = connections

    # ── Validation ────────────────────────────────────────────────────────────

    def validate(self) -> List[str]:
        """Return a list of human-readable problems. Empty list == valid graph."""
        problems: List[str] = []
        problems += self._validate_ports()
        if self.has_cycle():
            problems.append("Graph contains a cycle: a workflow must be a DAG (no loops).")
        return problems

    def _validate_ports(self) -> List[str]:
        problems: List[str] = []
        for (src, src_port), (dst, dst_port) in self.connections:
            if src not in self.blocks:
                problems.append(f"Connection references unknown source block '{src}'.")
                continue
            if dst not in self.blocks:
                problems.append(f"Connection references unknown target block '{dst}'.")
                continue
            if src_port not in self.blocks[src].outputs:
                problems.append(f"Block '{src}' has no output port '{src_port}'.")
            if dst_port not in self.blocks[dst].inputs:
                problems.append(f"Block '{dst}' has no input port '{dst_port}'.")
        return problems

    # ── Cycle detection ─────────────────────────────────────────────────────────

    def _adjacency(self) -> Dict[str, List[str]]:
        adj: Dict[str, List[str]] = {b: [] for b in self.blocks}
        for (src, _), (dst, _) in self.connections:
            if src in adj and dst in self.blocks:
                adj[src].append(dst)
        return adj

    def has_cycle(self) -> bool:
        """Detect a cycle via Kahn's algorithm (if we can't sort everything, there's a cycle)."""
        try:
            self.topological_order()
            return False
        except ValueError:
            return True

    # ── Topological sort (Kahn's algorithm) ──────────────────────────────────────

    def topological_order(self) -> List[str]:
        """Return block ids in a valid execution order. Raises ValueError on a cycle."""
        adj = self._adjacency()
        indegree: Dict[str, int] = {b: 0 for b in self.blocks}
        for src in adj:
            for dst in adj[src]:
                indegree[dst] += 1

        # Sort the ready set for a deterministic, reproducible order.
        ready = deque(sorted(b for b, d in indegree.items() if d == 0))
        order: List[str] = []
        while ready:
            node = ready.popleft()
            order.append(node)
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    ready.append(nxt)
            ready = deque(sorted(ready))

        if len(order) != len(self.blocks):
            raise ValueError("Cycle detected: no valid topological ordering exists.")
        return order


def _demo() -> None:
    blocks = [
        Block("load", "Load Image", inputs=[], outputs=["image"]),
        Block("resize", "Resize", inputs=["image"], outputs=["image"], config={"size": 640}),
        Block("gray", "Grayscale", inputs=["image"], outputs=["image"]),
        Block("detect", "Detect Objects", inputs=["image"], outputs=["detections"],
              config={"confidence_threshold": 0.5}),
        Block("alert", "Alert", inputs=["detections"], outputs=["event"]),
        Block("save", "Save Result", inputs=["detections"], outputs=[]),
    ]
    connections: List[Connection] = [
        (("load", "image"), ("resize", "image")),
        (("resize", "image"), ("gray", "image")),
        (("gray", "image"), ("detect", "image")),
        (("detect", "detections"), ("alert", "detections")),
        (("detect", "detections"), ("save", "detections")),
    ]

    graph = WorkflowGraph(blocks, connections)
    problems = graph.validate()
    print("Validation:", "VALID" if not problems else problems)
    print("Execution order:", " -> ".join(graph.topological_order()))

    print("\nNow add a cycle (save -> load) ...")
    bad = WorkflowGraph(blocks, connections + [(("save", "detections"), ("load", "image"))])
    # 'save' has no 'detections' output and 'load' has no 'image' input -> port + cycle problems.
    print("Validation:", bad.validate())


if __name__ == "__main__":
    _demo()
