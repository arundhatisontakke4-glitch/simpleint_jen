import sys

def simple_interest(p, r, t):
    return (p * r * t) / 100

if __name__ == "__main__":
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])

    si = simple_interest(principal, rate, time)

    print("Simple Interest:", si)