# A000268

> E.g.f.: -log(1+log(1+log(1-x))).
> — [OEIS A000268](https://oeis.org/A000268)

Offset 1: 1, 3, 15, 105, 947, 10472, 137337, 2085605, 36017472, 697407850, …

a(n) is the number of ways to arrange n labelled objects as a cycle of
cycles of cycles, since −log(1 − x) is the e.g.f. of a single cycle.

### Python 3 — 85 bytes

```python
Q=[[s:=1]]*3
while[print(s)]:s=0;Q=[[s:=s+i*e for i,e in enumerate([0]+E)]for E in Q]
```

**How it works**

- With L(t) = −log(1 − t), 1 + log(1 − x) = 1 − L(x), so the e.g.f. is
  L(L(L(x))). Putting L into an e.g.f. X is the Stirling transform
  y(n) = Σ_k c(n,k)·x(k), with c the unsigned Stirling numbers of the
  first kind (L^k/k! is the e.g.f. of column k). So a is that transform
  applied three times to the identity, x(n) = [n = 1]; this is Kruchinin's
  double Stirling sum in the OEIS entry.
- The transform can be run online, one input at a time. Let
  U(i,m) = Σ_k c(i,k)·x(k+m). From c(i+1,k) = i·c(i,k) + c(i,k−1),
  U(i+1,m) = i·U(i,m) + U(i,m+1), with U(0,m) = x(m) and y(i) = U(i,0).
  Keep the antidiagonal E = [U(1,N−1), …, U(N,0)] (U(0,N) only ever gets
  the weight 0, so it is dropped). When x(N+1) arrives, the next
  antidiagonal is a running sum: s = x(N+1), then s += i·E[i−1] for
  i = 1..N, and its last entry is y(N+1). That is
  `[s:=s+i*e for i,e in enumerate([0]+E)]`: the 0 has weight 0, so the
  first entry is the input itself and the list grows by one.
- `Q` holds the three antidiagonals. The walrus `s` runs through all of
  them in one outer comprehension, so each level's output is the next
  level's input, and after the pass `s` is a(N+1).
- The identity is 1 at n = 1 and 0 afterwards. Every level equals 1 at
  n = 1, so the loop starts with all three antidiagonals at `[1]` and
  `s` = a(1) = 1, and then feeds 0 (`s=0`). The first level is just a
  factorial generator: its antidiagonal is [0, …, 0, (N−1)!].

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (400 terms) prints in 0.2 s and matches; the first 60 terms also match
  Kruchinin's sum computed independently from a Stirling table. The
  program prints 1412 terms in about 4 s and then stops, when a(1413)
  passes the 4300-digit int-to-str limit of Python 3.11+. The bar is the
  whole b-file in 60 s.
- The `s=0` cannot go: each level adds its input to its output with
  coefficient 1, so a carried-over s leaks into every later term (with
  a(N) fed back into the first level, the loop would print X′ − 1 for the
  solution of X′ = 1 + L(L(L(X)))). Every way found to reset s inside the
  comprehension was longer, and so is feeding (N−1)! straight into two
  levels, which needs a counter (`s=f=f*n;n+=1;`).
- Working with rows of c(n,k) instead (multiply by x + n each step, then
  take dot products with the stored values of the level below) needs all
  three levels kept in full and comes out much longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000268), CC BY-SA 4.0.
