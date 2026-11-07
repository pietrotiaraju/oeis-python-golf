# A000904

> a(n) = (n+1)*a(n-1) + (n+2)*a(n-2) + a(n-3); a(1)=0, a(2)=3, a(3)=13.
> — [OEIS A000904](https://oeis.org/A000904)

Offset 1: 0, 3, 13, 83, 592, 4821, 43979, 444613, 4934720, 59661255, …

### Python 3 — 52 bytes

```python
a,b=0,1;m=3
while[print(a)]:m+=1;a,b=m*a+b+2-m%2*4,a
```

**How it works**

- Lucas's two-term form (on the OEIS page, from Shevelev):
  a(n) = (n+2)·a(n−1) + a(n−2) + 2·(−1)ⁿ for n ≥ 3. It defines the same
  sequence: if e(n) is its left side minus its right side, the three-term
  recurrence gives e(n) + e(n−1) = 0, and e(3) = 13 − 15 − 0 + 2 = 0, so
  e(n) = 0 for every n ≥ 3.
- Run backwards it gives a virtual a(0) = 1 (from a(2) = 4·0 + a(0) + 2),
  so the loop starts with `a,b` = a(1), a(0) = 0, 1 and the two-term form
  already holds at n = 2.
- `m` is n+2, which has the parity of n, so the sign term 2·(−1)ⁿ is
  `2-m%2*4` (2 for even m, −2 for odd m).
- Tracking A(n) = (−1)ⁿa(n) instead removes the sign term
  (A(n) = −(n+2)A(n−1) + A(n−2) + 2) but needs `abs` on output: also
  52 bytes. The three-term recurrence itself, with the negated-state trick of
  [A000179](../A000179/), is 57.

**Notes**

- Exact integer arithmetic, correct for every n; checked against the
  three-term recurrence up to a(1556).
- The b-file has 100 terms (up to a(100)); the bar is the whole b-file in
  60 s. The program prints 1556 terms at once and then stops with a
  `ValueError` at the 4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000904), CC BY-SA 4.0.
