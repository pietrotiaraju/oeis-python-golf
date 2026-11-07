# A000630

> Number of ways to represent n using the binary operator a * b = 2^a + b.
> — [OEIS A000630](https://oeis.org/A000630)

Offset 0: 1, 1, 2, 3, 7, 12, 23, 41, 81, 149, 282, 522, 987, …

### Python 3 — 76 bytes

```python
d={0:1};n=0
while[print(d[n])]:n+=1;d[n]=sum(d[j]*d.get(n-2**j,0)for j in d)
```

**How it works**

- The OEIS generating function is Σ a(n)qⁿ = 1/(1 − Σⱼ a(j)q^(2ʲ)).
  Writing A = 1/(1 − B) as A = 1 + B·A gives a(0) = 1 and, for n ≥ 1,
  a(n) = Σ a(j)·a(n − 2ʲ) over the j with 2ʲ ≤ n. In words: the outermost
  a * b of a representation of n is 2ʲ + (n − 2ʲ), with a(j) choices for the
  exponent and a(n − 2ʲ) for the rest (0 being the empty rest).
- `d` maps k to a(k) for every k < n. The sum runs over all stored j and
  takes `d.get(n-2**j,0)`: when 2ʲ > n the key is negative, not in `d`, and
  counts 0, so only the j with 2ʲ ≤ n contribute. Those j are below n, so
  d[j] is already known.
- A list would wrap a negative index around to a real term; the dict with a
  default 0 is what makes an out-of-range index mean "no term".
- `while[print(d[n])]:` prints the newest term; a one-element list is always
  true.

**Notes**

- Exact integer arithmetic, so the program is right for every n. It builds
  2ʲ for every j < n at each step, which is wasteful (about 5000 terms in
  60 s) but does not matter here.
- Bounding j by the bit length instead,
  `a+=sum(a[j]*a[-2**j]for j in range(len(bin(len(a)))-2)),` on a list, is
  82 bytes.
- The b-file has the 36 terms of the OEIS entry; the bar is all 36 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000630), CC BY-SA 4.0.
