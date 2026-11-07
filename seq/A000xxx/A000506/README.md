# A000506

> One half of the number of permutations of [n] such that the differences have 5 runs with the same signs.
> — [OEIS A000506](https://oeis.org/A000506)

Offset 6: 61, 841, 7311, 51663, 325446, 1910706, 10715506, 58258210, 309958755, 1623847695, …

An alternating run of a permutation is a maximal stretch of consecutive
differences with the same sign; a(n) is half the number of permutations of
1..n with exactly 5 of them (the count is even since reversal pairs them up).

### Python 3 — 94 bytes

```python
b=c=d=e=0;m=-2
while[e>0==print(e)]:m+=1;b,c,d,e=2*b+2,3*c+2*b+m+1,4*d+2*c+m*b,5*e+2*d+(m-1)*c
```

**How it works**

- Put n into one of the n gaps of a permutation of 1..n−1 with r alternating
  runs: r gaps keep r runs, 2 gaps give r + 1 and the other n − r − 2 give
  r + 2 (André 1884; see Bóna, *Combinatorics of Permutations*, ch. 1; a
  brute force over n ≤ 8 confirms the gap counts). So the halved counts
  p(n, k) satisfy

  p(n, k) = k·p(n−1, k) + 2·p(n−1, k−1) + (n − k)·p(n−1, k−2),

  the recurrence in the OEIS entry, and a(n) = p(n, 5).
- p(n, 1) = 1 for n ≥ 2 (the increasing and the decreasing permutation,
  halved), and p(n, 0) = 0, so the program keeps only k = 2…5 in `b,c,d,e`.
  At n = 2 they are all 0. With m = n − 4 the new row is
  b = 2b + 2, c = 3c + 2b + (m + 1), d = 4d + 2c + m·b and
  e = 5e + 2d + (m − 1)·c, all read from the old row by the tuple
  assignment; `m=-2` is the value before the first step to n = 3.
- `e>0==print(e)` prints only once e = p(n, 5) is nonzero, which is from
  n = 6 on (5 runs need at least 6 elements); `[False]` keeps the loop going.

**Notes**

- A list of six columns updated by a comprehension, as in the Mathematica
  program of the entry, was 116 bytes. Other offsets of m tie or lose.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 18 terms (up to a(23)); the bar is the whole b-file in
  60 s.
- Python's 4300-digit int-to-str limit stops the printing after a(6153)
  (4300 digits; a(6154) has 4301), about a second after the start.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 116 | first entry |
| 2026-11-07 | Python 3 | 94 | four named columns instead of a list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000506), CC BY-SA 4.0.
