from brian2 import *
from brian2.devices.cpp import *
import os

eqs = '''
dV/dt = -V/(10*ms) : 1
'''

G = NeuronGroup(10, eqs)
G.V = 1

net = Network(G)

net.run(100*ms)

#print '%g'%G.V[0]

insert_code('''
    cout << "Next two lines should be the same:\\n4.53999e-005\\n";
    cout << neurongroup_0.arrays["V"][0] << endl;
''')

build(run=True)
