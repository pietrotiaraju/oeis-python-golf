# A001000

> a(n) = least m such that if a/b < c/d where a,b,c,d are integers in [0,n], then a/b < k/m < c/d for some integer k.
> — [OEIS A001000](https://oeis.org/A001000)

Offset 1: 2, 3, 5, 7, 13, 17, 26, 31, 43, 57, 65, 82, 101, 111, 133, 157, 183, …

### Python 3 — 52 bytes

```python
w=s=1
while 1:w+=2;s+=s*s+6<2*w;print((w-s)**2//4+1)
```

**Why the formula**

- Only consecutive Farey fractions of order n matter (a comment in the
  entry): a gap between fractions above 1 lies in some [i, i+1], and
  subtracting i turns its ends into fractions of [0, 1] with denominators
  ≤ n, so it contains a whole Farey gap u < v; a point k/m between u and v
  gives (im + k)/m inside the original gap.
- Rustem Aidagulov and Max Alekseyev ("Proof that A001000 and A071111 are
  essentially the same sequence", linked from the entry) prove that for
  n > 1 the multiples of 1/m separate Farey(n) exactly when they separate
  {1, 1/2, …, 1/n}, and (their Theorem 2) that the least such m is
  n(n − t) + ⌊t²/4⌋ + 1 with t = ⌊√(4n − 5)⌋. This is Herzig's formula for
  Crux problem 2272 and Wilson's formula in the entry.
- n(n − t) + ⌊t²/4⌋ = ⌊(2n − t)²/4⌋. For n = 1 the only gap is 0 < 1, so
  a(1) = 2, which the same expression gives with t = 0.

**How it works**

- `w` = 2n + 1 and `s` = t + 1. Each pass adds 2 to `w`, and 1 to `s` when
  s² ≤ 4n − 5, written `s*s+6<2*w`. That keeps s = ⌊√(4n − 5)⌋ + 1: 4n − 5
  grows by 4 per step, and once t ≥ 1 the next square but one is at least
  2t + 3 > 4 further, so s never has to move twice (the first step, from
  t = 0 to t = 1, is checked directly).
- `w-s` = 2n − t, so the term is `(w-s)**2//4+1`.
- Printing after the update lets both start at 1 (`w=s=1` is a phantom
  n = 0): 1 byte under `while[print(…)]:` with `w=3;s=1`.

**Notes**

- Integer arithmetic only, no square roots; correct for every n by the
  Aidagulov–Alekseyev theorem.
- Hundreds of thousands of terms in 10 s; the b-file has 1000 terms and
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001000), CC BY-SA 4.0.
