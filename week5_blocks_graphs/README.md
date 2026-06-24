# Week 5 : Blocks & Graphs

**Focus:** blocks, ports, connections, graph validation, topological sorting.

## Build a block graph and validate it
`graph_validation.py` models a workflow as a directed graph of `Block`s connected by port-to-port
`Connection`s, and provides:
- `WorkflowGraph.validate()` : returns a list of problems (empty == valid).
- `WorkflowGraph.has_cycle()` : true if the graph is not a DAG.
- `WorkflowGraph.topological_order()` : a valid execution order (Kahn's algorithm), or raises on a cycle.

The demo builds the pipeline **Load → Resize → Grayscale → Detect → {Alert, Save}**, validates it,
prints the execution order, then shows what happens when a cycle is introduced.

```bash
python graph_validation.py
```

## Homework — graph validation checklist
Encoded as tests in `test_graph_validation.py`. A valid block graph must:
1. Reference only blocks that exist.
2. Use only ports that exist on those blocks.
3. Be acyclic (a DAG) : no block depends on itself.
4. Have a valid execution order where each block runs after its dependencies.

```bash
pytest test_graph_validation.py -v
```

## Why validation must happen *before* execution
A cycle means there is no first block to run — the workflow can never start. An edge to a
non-existent port means data has nowhere to go. Catching these statically (before running any
handler) is far cheaper and safer than discovering them mid-execution.
