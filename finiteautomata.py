def compute_transition_function(P):
    m = len(P)
    alphabet = list(set(P))
    delta = []
    for state in range(m + 1):
        row = {}
        for a in alphabet:
            row[a] = 0
        delta.append(row)


    for q in range(m + 1):
        for a in alphabet:

            k = min(m+1, q +2)

            while True:
                k -= 1
                candidate = P[:q] + a
                if candidate.endswith(P[:k]):
                    break

            delta[q][a] = k

    return delta, alphabet


def finite_automaton_matcher(T, P):
    n= len(T)
    m = len(P)

    delta, alphabet = compute_transition_function(P)
    q = 0

    for i in range(n):
        c = T[i]

        if c in alphabet:
            q = delta[q][c]
        else:
            q = 0

        if q == m:
            print("Pattern occurs in shift", i - m + 1)



T ="ababaabababa"
P = "aba"

print("Text:", T)
print("Pattern:", P)
print("\nMatches:")
finite_automaton_matcher(T, P)
