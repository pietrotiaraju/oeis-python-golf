# A000558

> Generalized Stirling numbers of second kind.
> — [OEIS A000558](https://oeis.org/A000558)

Offset 2: 1, 6, 32, 175, 1012, 6230, 40819, 283944, 2090424, 16235417, …

a(n) = Σ_k S(n, k)·S(k, 2), with S the Stirling numbers of the second kind:
split n labelled items into blocks, then split the blocks into two
non-empty groups. The e.g.f. is (exp(e^x − 1) − 1)²/2.

### Python 3 — 76 bytes

```python
L=[0]
while 1:L=[s:=~-2**len(L)]+[s:=s+len(L)*L.pop(0)for _ in L*1];print(s)
```

**How it works**

- **A triangle for Σ S(n, k)·c_k.** Since (e^x − 1)^k/k! = Σ_n S(n, k)·xⁿ/n!,
  a(n) is n! [xⁿ] Φ(u) with u = e^x − 1 and Φ(u) = Σ_m c_m·u^m/m!,
  c_m = S(m, 2) = 2^(m−1) − 1. Differentiating in x is (1 + u)·d/du (as
  u′ = 1 + u), and on u^m/m! it gives u^(m−1)/(m−1)! + m·u^m/m!. So the
  coefficients T(j, m) of the j-th derivative in that basis satisfy

  T(j, m) = T(j − 1, m + 1) + m·T(j − 1, m),  T(0, m) = c_m,

  and a(n) = T(n, 0). This is Heinz's recurrence on the OEIS page.
- **Antidiagonals.** T(j, m) needs T(j − 1, m + 1), on the same antidiagonal
  j + m, and T(j − 1, m), on the previous one. Since T(j, 0) = T(j − 1, 1),
  the last entry of an antidiagonal repeats the one before it, so `L` keeps
  only T(0, d), T(1, d − 1), …, T(d − 1, 1), d entries. The next one starts
  with T(0, d + 1) = c_{d+1} = 2^d − 1, which is `~-2**len(L)`, and each
  later entry is s + m·x, with x the next old entry and m = d, …, 1: that is
  `len(L)`, read just before `L.pop(0)` removes x (the loop runs over the
  copy `L*1`). The last s is T(d, 1) = T(d + 1, 0) = a(d + 1).
- `L=[0]` is the antidiagonal d = 1, T(0, 1) = S(1, 2) = 0, so the first
  pass prints a(2).

**Notes**

- Other versions: the head as a running `(c:=c-~c)` (c ↦ 2c + 1) with
  `L=[c:=0]` is 77 bytes; the first entries kept the head as `2**~-n-1`
  with a counter n: 94 and 86 bytes. [A000559](../A000559/) is the same
  triangle with c_m = S(m, 3).
- Exact integer arithmetic, so the program is right for every n.
- Each term costs O(n) big-number steps. a(1939) is the first term with
  more than 4300 digits, so printing stops there with Python's int-to-str
  limit, after about 7 s here. The b-file has 557 terms (up to a(558)); the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 94 | first entry |
| 2026-11-06 | Python 3 | 86 | seed the zero antidiagonal and begin at the output offset |
| 2026-11-07 | Python 3 | 76 | head 2^d − 1 from len(L), weights from len(L) before pop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000558), CC BY-SA 4.0.
