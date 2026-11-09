# A001351

> Associated Mersenne numbers.
> — [OEIS A001351](https://oeis.org/A001351)

Offset 0: 0, 1, 3, 1, 3, 11, 9, 8, 27, 37, 33, 67, 117, 131, 192, 341, 459, 613, …

### Python 3 — 63 bytes

```python
L=[3,1,1]
while[print(L[-3]-L[0])]:L=[L[2]-L[1],*L,L[-1]+L[-3]]
```

**How it works**

- a(n) = (αⁿ − 1)(βⁿ − 1)(γⁿ − 1) for the roots α, β, γ of x³ − x² − 1
  (Bala's formula in the entry). Expanding, with αβγ = 1:
  a(n) = 1 − Σ(αβ)ⁿ + Σαⁿ − 1 = s(n) − s(−n), where s(m) = αᵐ + βᵐ + γᵐ
  (because αβ = 1/γ). The power sums obey s(m+3) = s(m+2) + s(m) for every
  integer m, with s(0), s(1), s(2) = 3, 1, 1.
- The list `L` holds s(−n), …, s(n+2). Each pass prints
  `L[-3]-L[0]` = s(n) − s(−n) and extends the window at both ends:
  forwards s(n+3) = s(n+2) + s(n) = `L[-1]+L[-3]`, backwards
  s(−n−1) = s(−n+2) − s(−n+1) = `L[2]-L[1]`.

**Notes**

- Two triples, `a,b,c,d,e,f=b,c,a+c,e,f,d-e` printing `a-d` (s and
  s(−n), whose recurrence is t(m+3) = t(m) − t(m+1)), take 70 bytes, and
  a window of six terms for the entry's order-6 recurrence is longer still.
- The list is rebuilt every pass, so the run is quadratic, but the
  6001-term b-file still takes well under a second.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 6001 terms (a(0) to a(6000)); the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001351), CC BY-SA 4.0.
