# A000559

> Generalized Stirling numbers of second kind.
> — [OEIS A000559](https://oeis.org/A000559)

Offset 3: 1, 12, 110, 945, 8092, 70756, 638423, 5971350, 57996774, 585092607, …

a(n) = Σ_k S(n, k)·S(k, 3), with S the Stirling numbers of the second kind:
split n labelled items into blocks, then split the blocks into three
non-empty groups. The e.g.f. is (exp(e^x − 1) − 1)³/6.

### Python 3 — 91 bytes

```python
L=[c:=0,e:=0]
while 1:L=[s:=(c:=3*c+(e:=e-~e))]+[s:=s+len(L)*L.pop(0)for _ in L*1];print(s)
```

**How it works**

- **The triangle.** As in [A000558](../A000558/), with u = e^x − 1 and
  c_m = S(m, 3), a(n) = T(n, 0) where T(0, m) = c_m and
  T(j, m) = T(j − 1, m + 1) + m·T(j − 1, m): differentiating in x is
  (1 + u)·d/du, which maps u^m/m! to u^(m−1)/(m−1)! + m·u^m/m!.
- **Antidiagonals.** T(j, 0) = T(j − 1, 1), so `L` keeps T(0, d), …,
  T(d − 1, 1). The next antidiagonal starts with c_{d+1}, and each later
  entry is s + m·x with m = d, …, 1, which is `len(L)` read just before
  `L.pop(0)` removes x; the last s is T(d + 1, 0) = a(d + 1).
- **The head.** S(m + 1, 3) = 3·S(m, 3) + S(m, 2) and S(m + 1, 2) =
  2·S(m, 2) + 1. `e-~e` is 2e + 1, and e is updated first, so
  `(c:=3*c+(e:=e-~e))` turns c = S(d, 3), e = S(d − 1, 2) into
  c = S(d + 1, 3), e = S(d, 2).
- `L=[c:=0,e:=0]` is the antidiagonal d = 2 (T(0, 2) = S(2, 3) = 0 and
  T(1, 1) = 0) with c = S(2, 3) = 0 and e = S(1, 2) = 0, so the first pass
  prints a(3).

**Notes**

- Other versions: the head `(c:=3*c+~-2**len(L)//2)` (S(d, 2) as
  ⌊(2^d − 1)/2⌋) with `L=[c:=0,0]` is 93 bytes; the first entries used
  `(3**n+3)//6-2**~-n` with a counter n: 104 and 98 bytes.
- Exact integer arithmetic, so the program is right for every n.
- Each term costs O(n) big-number steps. a(1914) is the first term with
  more than 4300 digits, so printing stops there with Python's int-to-str
  limit, after about 7 s here. The b-file has 20 terms (up to a(22)); the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 104 | first entry |
| 2026-11-06 | Python 3 | 98 | seed the zero antidiagonal and begin at the output offset |
| 2026-11-07 | Python 3 | 91 | running S(m, 3) and S(m, 2) as the head, weights from len(L) before pop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000559), CC BY-SA 4.0.
