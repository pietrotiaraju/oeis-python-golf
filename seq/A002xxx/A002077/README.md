# A002077

> Number of N-equivalence classes of self-dual threshold functions of exactly n variables.
> — [OEIS A002077](https://oeis.org/A002077)

Offset 1: 1, 0, 1, 4, 46, 1322, 112519, 32267168, …

### Python 3 — 372 bytes

```python
import math
n=0
while 1:V=Q=[[0]];exec('V=[v+[a+c for a in v]for v in V for c in range(v[len(v)//2],math.isqrt((n+1)**-~n)+2**n>>n)];Q=[q+[a+c for a in q]for q in Q for c in{1<<i for i in range(n)}-{*q}];'*n);print(len({(*map(f.__getitem__,q),)for f in{(*map(t.__lt__,v),)for v in V for t in v+[-1]}if f[::2]!=f[1::2]if{*map(sum,zip(f,f[::-1]))}-{1}=={2}for q in Q}));n+=1
```

**How it works**

- **One positive function per class.** A threshold function
  [w·x > t] on {0,1}ⁿ is unate: complementing the inputs with negative
  weight gives a positive (monotone) threshold function in its N-class
  (N-equivalence complements inputs). It is the only one: if f and f′ are
  both positive and f′ is f with the inputs in a set S complemented, f
  would increase and f′ decrease in every input of S that f depends on,
  so f depends on none of them and f′ = f.
- **What is counted.** Complementing inputs keeps a function self-dual,
  so a(n) is the number of positive self-dual threshold functions of n
  inputs that depend on all n inputs.
- **Self-dual functions from one input fewer.** Write fᵈ(x) = ¬f(x̄). If
  g is a positive self-dual threshold function of n inputs, f = g with
  xₙ = 1 is a positive threshold function of n − 1 inputs, g with xₙ = 0
  is fᵈ (self-duality), and fᵈ ≤ f because g is monotone in xₙ.
  Conversely, if f = [w·x > t] (integer weights, W = Σwᵢ) and fᵈ ≤ f,
  then fᵈ = [w·x > W − t − 1] and g = xₙf ∨ x̄ₙfᵈ is
  [w·x + (W − 2t − 1)xₙ > W − t − 1]: threshold, self-dual, and monotone
  since fᵈ ≤ f. So the positive self-dual threshold functions of n inputs
  correspond one to one to the positive threshold functions f of k = n − 1
  inputs with f(x) ∨ f(x̄) = 1 for every x, the inputs keeping their
  names. In the code `n` is k, and the program prints a(k + 1).
- **Exactly n inputs.** g = xₙf ∨ x̄ₙfᵈ depends on xₙ iff f ≠ fᵈ, and on
  another input iff f or fᵈ does, that is iff f does. With fᵈ ≤ f,
  f ≠ fᵈ means f(x) = f(x̄) = 1 for some x. So with s(x) = f(x) + f(x̄),
  the test is that every s(x) is 1 or 2 and some is 2:
  `{*map(sum,zip(f,f[::-1]))}-{1}=={2}` (point 2ᵏ − 1 − p is the
  complement of p). For n = 1, f is the constant 1 of no inputs and g is
  x₁. Both tests are kept by permutations of the inputs.
- **Weights.** Every threshold function of k inputs has integer weights
  with |wᵢ| ≤ B = ⌊(k+1)^((k+1)/2)/2ᵏ⌋ (Muroga, Toda and Takasu, 1961).
  For a positive f, raising the negative weights to 0 keeps the
  realization: where w·x > t the new sum is no smaller, and where
  w·x ≤ t, clearing the negatively weighted inputs of x gives a point
  x′ below x, where f is 0, and w·x′ is the new sum of x. With integer
  weights the threshold can be an integer, and t = −1 or one of the sums
  gives every cut. So the positive threshold functions of k inputs are
  exactly the [w·x > t] with 0 ≤ wᵢ ≤ B.
- **Sorted weights, then permutations.** Permuting the inputs puts the
  weights in order, so every positive threshold function is f∘π for some
  f with 0 ≤ w₁ ≤ … ≤ w_k ≤ B and a permutation π of the inputs. The
  program builds the set F of those f (one per NP-class, as on
  [A000617](../A000617/)), applies all k! permutations to each kept f and
  counts the distinct truth tables.
- **f depends on all k inputs.** With sorted weights, input 0 (the lightest) is
  the weakest: if f depends on it, f depends on every input. (Say
  f(y) = 0, f(y + e₀) = 1 and w₀ ≤ wⱼ. If yⱼ = 0, then y + eⱼ has sum at
  least that of y + e₀, so f(y + eⱼ) = 1 ≠ f(y). If yⱼ = 1, then
  z = y − eⱼ + e₀ has sum at most that of y, so f(z) = 0, while
  z + eⱼ = y + e₀ gives 1.) `f[::2]!=f[1::2]` compares f at the points
  that differ in bit 0, so it keeps exactly the f that depend on all
  inputs, and permuting the inputs keeps that property.
- **Code.** `exec` runs two doubling steps k times. For `V`, appending a
  weight c turns the list `v` of sums w·x into `v+[a+c for a in v]`; the
  new weight belongs to the next higher bit of the point index, and since
  `v[len(v)//2]` is the weight appended last, c runs upward from it and
  the weights come out sorted, bit 0 lightest.
  `math.isqrt((n+1)**-~n)+2**n>>n` is B + 1, computed exactly.
  `(*map(t.__lt__,v),)` is the truth table of [w·x > t]. `Q` is built the
  same way with the weights 1, 2, 4, …, 2^(k−1) in every order (c runs
  over the powers of two not yet among the sums), so each `q` maps every
  point to the point with its input bits permuted, and
  `(*map(f.__getitem__,q),)` is f with its inputs permuted.

**Notes**

- Exact integer arithmetic. Correctness for every n rests on the
  Muroga–Toda–Takasu weight bound and on the self-dualization above.
- k = 6 enumerates C(20, 6) = 38 760 sorted weight vectors on 64 points,
  and the permutations act on the 1113 functions of F (fewer after a
  filter): about 23 s here, under 200 MB. k = 7 would need C(39, 7) ≈ 15.4
  million sorted vectors on 128 points. The bar is the 7 terms
  n = 1 to 7 (k = 0 to 6) in 120 s; the b-file has the 9 terms of the entry.
- [A002080](../A002080/) counts n or fewer variables: A002080(n) = Σ C(n, k)·a(k).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 372 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002077), CC BY-SA 4.0.
