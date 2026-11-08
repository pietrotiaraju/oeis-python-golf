# A001083

> Length of one version of Kolakoski sequence {A000002(i)} at n-th growth stage.
> — [OEIS A001083](https://oeis.org/A001083)

Offset 1: 1, 2, 2, 3, 5, 7, 10, 15, 23, 34, 50, 75, 113, 170, 255, 382, 574, 863, 1293, 1937, …

### Python 3 — 73 bytes

```python
w=[2]
while[print(len(w))]:w=[x for k,d in enumerate(w)for x in[k%2+1]*d]
```

**How it works**

- The growth stages are the words of the entry's example, 2 → 11 → 12 →
  122 → 12211 → 1221121 → …: each word is read as a list of run lengths,
  and the runs are filled with 1, 2, 1, 2, … in turn, starting with 1. From
  the third stage on the words are prefixes of the Kolakoski sequence
  [A000002](../../A000xxx/A000002/), and a(n) is the length of the n-th
  word.
- The comprehension is that expansion: the k-th entry d of the word
  becomes d copies of `k%2+1`. The loop prints the length, then expands.

**Notes**

- Only list building, no arithmetic. Each stage is about 1.5 times as long
  as the one before (a(n) ≈ 0.58·1.5ⁿ, conjectured), and the list costs
  8 bytes per letter: a(41) = 9652397 letters take about 200 MB with the
  next word being built, and in 60 s the program gets to a(45) but holds
  about 1 GB.
- So the bar is set on a 10-second run: 41 terms print in 10 s and the bar
  is 32 terms in 10 s (they come in 0.3 s). The b-file has 102 terms, up to
  a(102) ≈ 5.3·10¹⁷, computed by Brent and Osborn's method for
  [A042942](https://oeis.org/A042942); words that long cannot be built.
- `bytes(…)` instead of the list comprehension keeps one byte per letter
  (33 MB in 10 s, the same 41 terms) for 5 bytes more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001083), CC BY-SA 4.0.
