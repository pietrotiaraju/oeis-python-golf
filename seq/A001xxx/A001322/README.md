# A001322

> Number of equivalence classes of n-valued Post functions of 2 variables under action of symmetric group S_2.
> — [OEIS A001322](https://oeis.org/A001322)

Offset 2: 12, 10206, 2148007936, 149011627197265625, …

An n-valued Post function of 2 variables is any map {0,…,n−1}² → {0,…,n−1};
S₂ swaps the two arguments, and the classes are the orbits. Below the
number of values is k.

### Python 3 — 47 bytes

```python
k=2
while[print(k**k**2+k**(k*-~k>>1)>>1)]:k+=1
```

**How it works**

- Burnside's lemma: the identity fixes all k^(k²) functions. The swap fixes
  the k points (x, x) and pairs up the other k² − k points, so it has
  (k² + k)/2 cycles and fixes k^((k²+k)/2) functions. Hence
  a(k) = (k^(k²) + k^(k(k+1)/2))/2 for every k.
- `k**k**2` is k^(k²) (powers group to the right), `k*-~k>>1` is
  k(k+1)/2, and `+` binds tighter than `>>`, so the last `>>1` halves the
  sum. Both powers have the parity of k, so the sum is even and the halving
  is exact. The loop starts at the offset k = 2.

**Notes**

- `while k:=k+1:print(…)` from k = 1 is 48 bytes.
- a(51) has 4442 digits, so printing it stops the program with Python's
  4300-digit int-to-str limit after 49 terms (k = 2 to 50).
- The b-file is synthesized from the 7 terms of the entry; they print at
  once, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001322), CC BY-SA 4.0.
