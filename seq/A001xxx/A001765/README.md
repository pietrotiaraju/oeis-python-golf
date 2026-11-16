# A001765

> Coefficients of iterated exponentials.
> — [OEIS A001765](https://oeis.org/A001765)

Offset 1: 1, 7, 77, 1155, 21973, 506989, 13761937, 429853851, 15192078027, 599551077881, …

### Python 3 — 85 bytes

```python
Q=[[s:=1]]*7
while[print(s)]:s=0;Q=[[s:=s+i*e for i,e in enumerate([0]+E)]for E in Q]
```

**How it works**

- With L(t) = −log(1 − t), 1 + log(1 − x) = 1 − L(x), so the seven nested
  logarithms are L applied seven times, L(L(L(L(L(L(L(x))))))). Putting L into
  an e.g.f. X is the Stirling transform y(n) = Σ_k c(n,k)·x(k), with c the
  unsigned Stirling numbers of the first kind (L^k/k! is the e.g.f. of
  column k). So a is that transform applied seven times to the identity
  x(n) = [n = 1].
- The program is the one of [A000268](../../A000xxx/A000268/) (three
  logarithms) with 7 levels instead of 3. Each level keeps the antidiagonal
  E = [U(1,N−1), …, U(N,0)] of U(i,m) = Σ_k c(i,k)·x(k+m); from
  c(i+1,k) = i·c(i,k) + c(i,k−1), U(i+1,m) = i·U(i,m) + U(i,m+1), so when
  x(N+1) arrives the next antidiagonal is the running sum
  `[s:=s+i*e for i,e in enumerate([0]+E)]`, whose last entry is y(N+1).
- `Q` holds the seven antidiagonals; the walrus `s` runs through them in
  one outer comprehension, so each level's output feeds the next, and after
  the pass `s` is a(N+1). Every level is 1 at n = 1, so all start at `[1]`
  with `s` = a(1) = 1; the identity then feeds 0 (`s=0`).

**Notes**

- Exact integer arithmetic, correct for every n. a(1301) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program
  (after about 10 s here).
- The b-file has 100 terms (a(1) to a(100)); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001765), CC BY-SA 4.0.
