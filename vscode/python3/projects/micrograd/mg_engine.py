class Value:
    """stores a single scalar value and its gradient"""
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.gradient = 0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label 

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')
        def _backward():
            self.gradient += out.gradient
            other.gradient += out.gradient
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')
        def _backward():
            self.gradient += other.data * out.gradient
            other.gradient += self.data * out.gradient
        out._backward = _backward
        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supports int/float powers"
        out = Value(self.data**other, (self,), f'**{other}')
        def _backward():
            self.gradient += (other * self.data**(other-1)) * out.gradient
        out._backward = _backward
        return out

    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')
        def _backward():
            self.gradient += (out.data > 0) * out.gradient
        out._backward = _backward
        return out

    def backward(self):
        # topo sort
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # apply chain rule
        self.gradient = 1
        for v in reversed(topo):
            v._backward()

    def __neg__(self): 
        return self * -1

    def __radd__(self, other): 
        return self + other

    def __sub__(self, other): 
        return self + (-other)

    def __rsub__(self, other): 
        return other + (-self)

    def __rmul__(self, other): 
        return self * other

    def __truediv__(self, other): 
        return self * other**-1

    def __rtruediv__(self, other): 
        return other * self**-1

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.gradient}, label={self.label})"
