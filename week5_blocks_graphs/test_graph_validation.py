"""Week 5 Homework — a graph-validation checklist, expressed as tests.

The checklist a valid block graph must pass:
  1. Every connection references blocks that exist.
  2. Every connection uses ports that actually exist on those blocks.
  3. The graph is acyclic (a DAG) — no block depends on itself.
  4. A valid execution order exists where each block runs after its dependencies.

Run:
    pytest test_graph_validation.py -v
"""

from graph_validation import Block, Connection, WorkflowGraph


def linear_graph():
    blocks = [
        Block("load", "Load Image", inputs=[], outputs=["image"]),
        Block("resize", "Resize", inputs=["image"], outputs=["image"]),
        Block("detect", "Detect", inputs=["image"], outputs=["detections"]),
    ]
    connections = [
        (("load", "image"), ("resize", "image")),
        (("resize", "image"), ("detect", "image")),
    ]
    return WorkflowGraph(blocks, connections)


def test_valid_graph_has_no_problems():
    assert linear_graph().validate() == []


def test_valid_graph_execution_order():
    assert linear_graph().topological_order() == ["load", "resize", "detect"]


def test_unknown_block_is_flagged():
    g = WorkflowGraph(
        [Block("a", "A", outputs=["x"])],
        [(("a", "x"), ("ghost", "y"))],
    )
    problems = g.validate()
    assert any("unknown target block 'ghost'" in p for p in problems)


def test_missing_port_is_flagged():
    g = WorkflowGraph(
        [Block("a", "A", outputs=["x"]), Block("b", "B", inputs=["y"])],
        [(("a", "x"), ("b", "WRONG"))],
    )
    problems = g.validate()
    assert any("no input port 'WRONG'" in p for p in problems)


def test_cycle_is_detected():
    blocks = [
        Block("a", "A", inputs=["in"], outputs=["out"]),
        Block("b", "B", inputs=["in"], outputs=["out"]),
    ]
    connections: list[Connection] = [
        (("a", "out"), ("b", "in")),
        (("b", "out"), ("a", "in")),  # back edge -> cycle
    ]
    g = WorkflowGraph(blocks, connections)
    assert g.has_cycle() is True
    assert any("cycle" in p.lower() for p in g.validate())


def test_diamond_graph_orders_dependencies_first():
    # load -> (resize, gray) -> detect
    blocks = [
        Block("load", "Load", outputs=["image"]),
        Block("resize", "Resize", inputs=["image"], outputs=["image"]),
        Block("gray", "Gray", inputs=["image"], outputs=["image"]),
        Block("detect", "Detect", inputs=["a", "b"], outputs=["det"]),
    ]
    connections = [
        (("load", "image"), ("resize", "image")),
        (("load", "image"), ("gray", "image")),
        (("resize", "image"), ("detect", "a")),
        (("gray", "image"), ("detect", "b")),
    ]
    order = WorkflowGraph(blocks, connections).topological_order()
    assert order.index("load") < order.index("resize")
    assert order.index("load") < order.index("gray")
    assert order.index("resize") < order.index("detect")
    assert order.index("gray") < order.index("detect")
