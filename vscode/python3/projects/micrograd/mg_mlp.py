import random
from mg_engine import Value

class Module:
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []

class Neuron(Module):
    def __init__(self, num_nodes, nonlinear=True):
        # Tag each weight with label='weight'
        self.w = [Value(random.uniform(-1,1), label='weight') for _ in range(num_nodes)]
        # Tag bias with label='bias'
        self.b = Value(0, label='bias')
        self.nonlinear = nonlinear

    def __call__(self, x):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        return act.relu() if self.nonlinear else act

    def parameters(self):
        return self.w + [self.b]

    def __repr__(self):
        return f"{'ReLU' if self.nonlinear else 'Linear'} Neuron({len(self.w)})"

class Layer(Module):

    def __init__(self, num_nodes, nodes_out, **kwargs):
        self.neurons = [Neuron(num_nodes, **kwargs) for _ in range(nodes_out)]

    def __call__(self, x):
        out = [n(x) for n in self.neurons]
        return out[0] if len(out) == 1 else out

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

class MLP(Module):

    def __init__(self, num_nodes, nodes_out):
        sz = [num_nodes] + nodes_out
        self.layers = [Layer(sz[i], sz[i+1], nonlinear=i!=len(nodes_out)-1) for i in range(len(nodes_out))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"