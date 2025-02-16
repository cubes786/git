import random
from graphviz import Digraph
from IPython.display import display, SVG
from mg_engine import Value
import mg_mlp 


def dfsWalk(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges


def draw_dot(root, format='svg', rankdir='LR'):
    nodes, edges = dfsWalk(root)
    dot = Digraph(format=format, graph_attr={'rankdir': rankdir}, node_attr={'rankdir': 'TB'})

    for n in nodes:
        # Decide shape/color by label
        if n.label == 'weight':
            shape = 'ellipse'
            color = 'lightblue'
        elif n.label == 'bias':
            shape = 'ellipse'
            color = 'pink'
        elif n.label == 'input':
            shape = 'box'
            color = 'lightyellow'
        else:
            shape = 'record'
            color = 'white'
        # Build a custom label that includes the Value's label + data + gradient
        node_label = f"{n.label if n.label else 'Value'} | data={n.data:.4f} | grad={n.gradient:.4f}"
        dot.node(
            name=str(id(n)),
            label="{" + node_label + "}",
            shape=shape,
            style='filled',
            fillcolor=color
        )
      
        # If this Value was created by an operation, create a separate op node
        if n._op:
            dot.node(name=str(id(n)) + n._op, label=n._op, shape='circle')
            dot.edge(str(id(n)) + n._op, str(id(n)))

    for n1, n2 in edges:
        # n1 --> op node --> n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot

random.seed(786)
# Create a single neuron with ReLU
#n = mg_mlp.Neuron(num_nodes=2, nonlinear=True)
mlp = mg_mlp.MLP(num_nodes=2, nodes_out=[2, 1])

# Create input Value objects (with labels, if using the labeling extension)
x = [Value(1.0, label='input'), Value(-2.0, label='input')]

# Forward pass: compute the output of the MLP.
output = mlp(x)

# For testing, define a simple loss as the output itself if scalar,
# or sum the outputs if output is a list.
loss = output if isinstance(output, Value) else sum(output)

# Backward pass: compute gradients through backpropagation.
loss.backward()

# Draw
dot=draw_dot(loss)

dot.render('example', view=True)

# Open the SVG file in a default web browser
import webbrowser
webbrowser.open('example.svg')
