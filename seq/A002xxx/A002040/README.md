# A002040

> Related to partitions.
> — [OEIS A002040](https://oeis.org/A002040)

Offset 0: 1, 2, 4, 8, 21, 52, 131, 316, 765, 1846, 4494, 10944, 26654, 64798, 157502, 382868, 931028, …

### Python 3 — 105 bytes

```python
H=[t:=1]
while[print(H[-1])]:H+=sum((1-(j&2))*~-g*H[g]for j in range(-t,t)if~t<(g:=j-j*3*j+2>>1)<0),;t+=1
```

**How it works**

- The g.f. is 1/f′(x) with f(x) = Π_{k>0} (1 − (−x)ᵏ) (Somos). By Euler's
  pentagonal number theorem f(x) = Σ_{j∈ℤ} (−1)^(j(3j+1)/2)·x^P(j) with
  P(j) = j(3j − 1)/2, and the sign is `1-(j&2)`: j(3j + 1)/2 is even
  exactly when j ≡ 0 or 1 (mod 4), and bit 1 of j (two's complement for
  negative j) is j mod 4 ≥ 2.
- So f′(x) = Σ_j f_P·P·x^(P−1) with f′(0) = 1 (j = 1), and the inverse
  series is **a(n) = −Σ_{2≤P≤n+1} P·f_P·a(n + 1 − P)**, a sum over the
  generalized pentagonal numbers 2, 5, 7, 12, 15, ….
- As in [A001482](../../A001xxx/A001482/), `g = j-j*3*j+2>>1` is 1 − P,
  so `H[g]` reads a(n + 1 − P) back from the end of the list, and
  `~t<g<0` (t = n terms so far) keeps exactly 2 ≤ P ≤ n + 1. The weight
  `(1-(j&2))*~-g` is f_P·(−P), which carries the minus sign.
- `range(-t,t)` holds every j with 2 ≤ P(j) ≤ n + 1 (here t = n): P grows
  with |j| on each side, P(t) = t(3t − 1)/2 > t + 1 for t ≥ 2, and
  P(−t − 1) > t + 1 for t ≥ 1; for t = 1 the only j needed is −1 (P = 2).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 301 terms (n = 0 to 300); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002040), CC BY-SA 4.0.
