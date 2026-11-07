# A000507

> Number of permutations of [n] with exactly 3 increasing runs of length at least 2.
> — [OEIS A000507](https://oeis.org/A000507)

Offset 6: 61, 1385, 19028, 206276, 1949762, 16889786, 137963364, 1081702420, 8236142455, 61386982075, …

### Python 3 — 71 bytes

```python
a=b=c=m=0
while[c>0==print(c)]:m+=1;a,b,c=3*a+m,5*b+(m-2)*a,7*c+(m-4)*b
```

**How it works**

- An increasing run of length ≥ 2 ends at a position i with
  π(i−1) < π(i) > π(i+1), where π(0) = +∞ and π(n+1) = −∞ (so a run cannot
  end at i = 1, and a run that reaches the end counts). Call these i peaks;
  T(n, k) counts permutations of 1..n with k peaks.
- Put n into one of the n gaps of a permutation of 1..n−1 with k peaks. At
  the front, n is no peak and nothing changes. In any other gap n becomes a
  peak, its two neighbours can no longer be peaks, and the count stays the same
  exactly when the gap is right before or right after an old peak. Peaks are
  never adjacent and never at position 1, so these are 2k distinct gaps
  other than the front, and 2k + 1 gaps in all keep k peaks; the other
  n − 2k − 1 add one. Hence

  T(n, k) = (2k + 1)·T(n−1, k) + (n − 2k + 1)·T(n−1, k−1),

  the recurrence of A008971 in the OEIS entry, and a(n) = T(n, 3).
- T(n, 0) = 1, so the program keeps k = 1, 2, 3 in `a,b,c`, all 0 at n = 1.
  With m = n − 1 the new row is a = 3a + m, b = 5b + (m − 2)·a and
  c = 7c + (m − 4)·b, read from the old row by the tuple assignment. Where
  m − 2k + 2 is negative, T(n−1, k−1) is 0, so zero seeds stay correct.
- `c>0==print(c)` prints only once c = T(n, 3) is nonzero, which is from
  n = 6 on; `[False]` is a true list, so the loop never ends.

**Notes**

- The closed form in the entry,
  (3·7ⁿ − (6n − 9)·5ⁿ + (6n² − 18n + 3)·3ⁿ − 4n³ + 18n² − 8n − 15)/192,
  is 90 bytes with `while[print(…)]:n+=1` (91 with `while 1:`). It follows
  from the same recurrence by solving the columns k = 1, 2, 3 in turn.
- Exact integer arithmetic, so the program is right for every n; a brute
  force over all permutations agrees for n ≤ 9.
- The b-file has 18 terms (up to a(23)); the bar is the whole b-file in
  60 s.
- Python's 4300-digit int-to-str limit stops the printing after a(5090)
  (4300 digits; a(5091) has 4301), about a second after the start.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |
| 2026-11-07 | Python 3 | 71 | peak recurrence on three columns |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000507), CC BY-SA 4.0.
