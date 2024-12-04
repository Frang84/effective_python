from argparse import ArgumentParser
from sympy import symbols, diff

# parser = ArgumentParser()

# parser.add_argument('squer', help='Echos given argument', type=int)

# parser.add_argument('-v', '--verbose', help='provides a verbose description', action='store_true')

# arguments = parser.parse_args()
# if arguments.verbose: 
#     print(f'{arguments.squer} squered is: {arguments.squer ** 2}')
# else: 
#     print(arguments.squer ** 2)


parser = ArgumentParser()

parser.add_argument('formula', help='euquesion to find solution of', type=str)
parser.add_argument('--start', '-s', help='point to start calculations', default=0, type=float)
parser.add_argument('--maxIteration', '-mi', help='maximum number of iterations', default=100, type=int)
parser.add_argument('--tolerance', '-t', help='tolerance', default=0.001, type=float)

args = parser.parse_args()

def newtonsMethod(f, start, tolerance, maxIteration): 
    xn = start 
    x = symbols('x')
    fDerivative = diff(f, x)
    f = eval(f)
    for i in range(maxIteration): 
        fx = f.subs(x, xn)
        fDx = fDerivative.subs(x, xn)
        if abs(fx) < tolerance: 
            return float(xn)
            #return xn
        if fDx == 0: 
            raise ValueError('fDx == 0')
        xn = xn - fx / fDx
    raise ValueError('i > maxIteration')

print(newtonsMethod(args.formula, args.start, args.tolerance, args.maxIteration))



