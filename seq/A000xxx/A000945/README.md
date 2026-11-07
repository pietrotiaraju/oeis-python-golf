# A000945

> Euclid-Mullin sequence: a(1) = 2, a(n+1) is smallest prime factor of 1 + Product_{k=1..n} a(k).
> — [OEIS A000945](https://oeis.org/A000945)

Offset 1: 2, 3, 7, 43, 13, 53, 5, 6221671, 38709183810571, 139, 2801, 11, 17, 5471, 52662739, 23003, 30693651606209, 37, …

### Python 3 — 60 bytes

```python
P=1
while 1:
 d=2
 while~P%d:d=-~[d,P][d*d>P]
 print(d);P*=d
```

**How it works**

- `P` is the product of the terms so far. `~P` is −(P+1), so `~P%d` is 0
  exactly when d divides P+1, and the program never needs P+1 itself.
- d counts up from 2. When d·d > P and d does not divide P+1, no d' ≤ √(P+1)
  divides P+1 (all smaller ones were tried), so P+1 is prime: then
  `-~[d,P][d*d>P]` jumps to P+1, which ends the loop; otherwise it is d+1.
  The final d is the smallest prime factor of P+1.

**Notes**

- Plain trial division with exact integers; no primality theorem is used.
- a(9) = 38709183810571 is P+1 itself, proved prime by the √ cutoff
  (about 6.2·10⁶ trials); a(15) = 52662739 alone takes about 30 s.
  a(17) = 30693651606209 is out of reach: trial division would need 3·10¹³
  steps, and a faster method (Pollard rho) would still have to prove that no
  smaller prime divides P+1.
- 16 terms in 60 s (the 16th at 35 s); the bar is 14 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000945), CC BY-SA 4.0.
