# A000556

> Expansion of exp(-x) / (1 - exp(x) + exp(-x)).
> — [OEIS A000556](https://oeis.org/A000556)

Offset 0: 1, 1, 5, 31, 257, 2671, 33305, 484471, 8054177, 150635551, …

a(n) is n! times the coefficient of xⁿ in e^(−x)/(1 − e^x + e^(−x)).

### Python 3 — 85 bytes

```python
M=[];a=b=1
while 1:M=[s:=a]+[s:=s+(s+M.pop(0))*len(M)for _ in M*1];a,b=b,a+b;print(s)
```

**How it works**

- **A rational function of u = e^x − 1.** With e^x = 1 + u, the numerator
  is e^(−x) = 1/(1 + u) and the denominator is
  1 − e^x + e^(−x) = (1 − u − u²)/(1 + u), so the e.g.f. is
  1/(1 − u − u²) = Σ_k F_{k+1}·u^k, with F the Fibonacci numbers.
- **Differentiating in u.** If G(x) = Φ(u(x)), then G′ = (1 + u)·Φ′(u),
  because u′ = e^x = 1 + u. Write the j-th derivative as Σ_k T(j, k)·u^k;
  applying (1 + u)·d/du gives

  T(j, k) = (k + 1)·T(j − 1, k + 1) + k·T(j − 1, k),  T(0, k) = F_{k+1},

  and a(n) = T(n, 0), since u = 0 at x = 0.
- **Antidiagonals.** T(j, k) depends on T(j − 1, k + 1), on the same
  antidiagonal j + k, and on T(j − 1, k), on the previous one. So `M` holds
  the antidiagonal T(0, d), T(1, d − 1), …, T(d, 0), and the next one is
  built from its top end: `[s:=a]` is T(0, d + 1) = F_{d+2}, and each later
  entry is s + k·(s + x) = (k + 1)·s + k·x with s the entry just made and x
  the next entry of the old antidiagonal. Its weight k runs d, …, 0, which is
  `len(M)` just after `M.pop(0)` removed x: the list being popped is the old
  `M`, while the loop runs over the copy `M*1`. The last s is T(d + 1, 0),
  the term that is printed.
- `a,b=b,a+b` steps the Fibonacci numbers; with `a=b=1` the heads `a` are
  F_1, F_2, F_3, … = 1, 1, 2, …, and the first pass prints T(0, 0) = 1.

**Notes**

- Other versions: the same triangle with a counter, `k=len(M)` and
  `(k:=k-1)`, is 87 bytes; the first entry, the recurrence
  a(n) = 1 + 2·Σ_{odd k<n} C(n, k)·a(n − k) with `math.comb`, was 103.
  [A000557](../A000557/) is the same program with `[s:=b]` (heads F_{k+2}).
- Exact integer arithmetic (only sums and products), so the program is
  right for every n.
- Each term costs O(n) big-number steps. a(1417) is the first term with
  more than 4300 digits, so printing stops there with Python's int-to-str
  limit, after about 4 s here. The b-file has 20 terms (up to a(19)); the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 103 | first entry |
| 2026-11-07 | Python 3 | 85 | e.g.f. as 1/(1 − u − u²), u = e^x − 1, triangle of (1 + u)·d/du |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000556), CC BY-SA 4.0.
