# A000048

> Number of n-bead necklaces with beads of 2 colors and primitive period n,
> when turning over is not allowed but the two colors can be interchanged.
> — [OEIS A000048](https://oeis.org/A000048)

Offset 0: 1, 1, 1, 1, 2, 3, 5, 9, 16, 28, 51, 93, 170, 315, 585, 1091, …

### Python 3 — 93 bytes

```python
a=[1];m=0
while[print(a[m])]:m+=1;a+=(2**~-m-sum(k*a[k]for k in range(1,m)if m%(2*k)==k))//m,
```

**How it works**

- For n ≥ 1, a(n) is also the number of binary Lyndon words of length n
  with an odd number of 1's (a comment on the OEIS page).
- Count the 2^(m−1) binary words of length m with an odd number of 1's by
  primitive period. A word with primitive period k is a Lyndon word of
  length k, rotated in one of k ways, repeated m/k times, so its weight is
  odd exactly when m/k and the Lyndon word's weight are odd. That gives
  Barry Smith's formula from the OEIS page: **Σ k·a(k) = 2^(m−1)** over the
  k | m with m/k odd.
- Solving for the k = m term gives **a(m) = (2^(m−1) − Σ k·a(k)) / m** over
  the smaller such k, so no Möbius function is needed.
- `m%(2*k)==k` is "k divides m with an odd quotient": for m = q·k, m mod 2k
  is k when q is odd and 0 when q is even, and it is never k when k ∤ m.
- `a=[1]` holds a(0) = 1, so `a[k]` is a(k); `range(1,m)` skips k = 0.
  `2**~-m` is 2^(m−1), and `a+=(…)//m,` appends a(m) as a one-tuple.
- `while[print(a[m])]` prints a(m), then loops forever because the list is
  non-empty.

**Notes**

- Each term checks m − 1 candidate divisors, so the whole b-file (3321
  terms, n up to 3320) prints in about 0.5 s; the bar is the whole b-file
  in 60 s.
- a(n) is about 2^(n−1)/n, so from about n = 14 300 its decimal form passes
  Python's 4300-digit int-to-str limit.
- `m/k%2==1` is 91 bytes, but it uses floats and is exact only while
  m < 2^53, so it is not accepted (as in [A000037](../A000037/)).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000048), CC BY-SA 4.0.
