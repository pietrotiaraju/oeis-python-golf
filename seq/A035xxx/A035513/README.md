# A035513

> Wythoff array read by falling antidiagonals.
> — [OEIS A035513](https://oeis.org/A035513)

Offset 1: 1, 2, 4, 3, 7, 6, 5, 11, 10, 9, 8, 18, 16, 15, 12, …

### Python 3 — 89 bytes

```python
l=[0];R=[]
for d in l:R=[(y,print(x+y)or x+y)for x,y in R+[(len(R),len(l))]];l+=(1,0)[d:]
```

**How it works**

- Every row of the Wythoff array is a Fibonacci-type sequence,
  T(n,k) = T(n,k−1) + T(n,k−2), and run two steps to the left it starts
  T(n,−1) = n − 1, T(n,0) = ⌊nφ⌋ (R. J. Mathar's formula on the OEIS page;
  the same as Bottomley's T(n,k) = F(k+1)·⌊nφ⌋ + F(k)·(n−1)).
- `R` holds one pair (T(n,k−1), T(n,k)) for each row started so far.
  Antidiagonal d is T(1,d), T(2,d−1), …, T(d,1). Each pass adds the seed
  pair (d−1, ⌊dφ⌋) of row d at the end, moves every pair one step right
  with (x, y) → (y, x+y), and prints the new y on the way. The rows come out
  in order and the new row ends the pass with T(d,1) = ⌊dφ⌋ + d − 1, so one
  pass prints exactly one antidiagonal.
- The seed costs no counters: `len(R)` is d − 1 (one pair per earlier row),
  and `len(l)` is ⌊dφ⌋ because `l` is the queue of the
  [A000201](../../A000xxx/A000201/) program. It is the Fibonacci word
  0100101001… (0 for a gap of 2 between consecutive ⌊nφ⌋, 1 for a gap of 1);
  reading letter d appends `(1,0)[d:]`, i.e. 10 for a 0 and 0 for a 1, so
  the list grows by exactly the gap ⌊(d+1)φ⌋ − ⌊dφ⌋ on every pass.
- `print(x+y)or x+y` prints the new term and keeps it (`print` returns
  `None`), 10 bytes under a separate `[print(y)for x,y in R]`.

**Notes**

- Only integer additions, so it is exact for every n. Correctness rests on
  the seed formula above and on the classical fact behind A000201 that the
  zeros of the Fibonacci word sit at ⌊nφ⌋.
- The b-file has 5151 terms, the first 101 antidiagonals; the bar is all of
  them in 60 s, and the program prints about 300000 terms in 3 s. The
  4300-digit `int`-to-`str` limit would first hit T(1,d) = F(d+1) at
  d ≈ 20577, after about 2·10⁸ terms.
- Longer routes: one number per row with T(n,k+1) = ⌊(T(n,k)+1)φ⌋ − 1
  (true for k ≥ 1) needs `isqrt` and a separate append for column 1, whose
  entries are exactly the numbers that map never produces (120 bytes); two
  lists for the last two antidiagonals of the extended array, 101; seeding
  ⌊nφ⌋ with `isqrt` instead of the queue, 102; printing the old y and
  appending pre-advanced seeds, 92.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A035513), CC BY-SA 4.0.
