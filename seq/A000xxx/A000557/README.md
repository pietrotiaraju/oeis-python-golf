# A000557

> Expansion of e.g.f. 1/(1 - 2*sinh(x)).
> — [OEIS A000557](https://oeis.org/A000557)

Offset 0: 1, 2, 8, 50, 416, 4322, 53888, 783890, 13031936, 243733442, …

### Python 3 — 85 bytes

```python
M=[];a=b=1
while 1:M=[s:=b]+[s:=s+(s+M.pop(0))*len(M)for _ in M*1];a,b=b,a+b;print(s)
```

**How it works**

- **A rational function of u = e^x − 1.** 2 sinh x = e^x − e^(−x), and with
  e^x = 1 + u, 1 − e^x + e^(−x) = (1 − u − u²)/(1 + u). So the e.g.f. is
  (1 + u)/(1 − u − u²) = Σ_k F_{k+2}·u^k, with F the Fibonacci numbers
  (it is e^x times the e.g.f. of [A000556](../A000556/)).
- **Differentiating in u.** If G(x) = Φ(u(x)), then G′ = (1 + u)·Φ′(u),
  because u′ = e^x = 1 + u. Write the j-th derivative as Σ_k T(j, k)·u^k;
  applying (1 + u)·d/du gives

  T(j, k) = (k + 1)·T(j − 1, k + 1) + k·T(j − 1, k),  T(0, k) = F_{k+2},

  and a(n) = T(n, 0), since u = 0 at x = 0.
- **Antidiagonals.** T(j, k) depends on T(j − 1, k + 1), on the same
  antidiagonal j + k, and on T(j − 1, k), on the previous one. So `M` holds
  the antidiagonal T(0, d), T(1, d − 1), …, T(d, 0), and the next one is
  built from its top end: `[s:=b]` is T(0, d + 1) = F_{d+3}, and each later
  entry is s + k·(s + x) = (k + 1)·s + k·x with s the entry just made and x
  the next entry of the old antidiagonal. Its weight k runs d, …, 0, which is
  `len(M)` just after `M.pop(0)` removed x: the list being popped is the old
  `M`, while the loop runs over the copy `M*1`. The last s is T(d + 1, 0),
  the term that is printed.
- `a,b=b,a+b` steps the Fibonacci numbers; with `a=b=1` the heads `b` are
  F_2, F_3, F_4, … = 1, 2, 3, …, and the first pass prints T(0, 0) = 1.

**Notes**

- Other versions: the same triangle with a counter, `k=len(M)` and
  `(k:=k-1)`, is 87 bytes; the first entry, the recurrence
  a(n) = 2·Σ_{odd k≤n} C(n, k)·a(n − k) for n ≥ 1 with `math.comb`, was 103.
  [A000556](../A000556/) is the same program with `[s:=a]`.
- Exact integer arithmetic (only sums and products), so the program is
  right for every n.
- Each term costs O(n) big-number steps. a(1417) is the first term with
  more than 4300 digits, so printing stops there with Python's int-to-str
  limit, after about 4 s here. The b-file has 201 terms (up to a(200)); the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 103 | first entry |
| 2026-11-07 | Python 3 | 85 | e.g.f. as (1 + u)/(1 − u − u²), u = e^x − 1, triangle of (1 + u)·d/du |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000557), CC BY-SA 4.0.
