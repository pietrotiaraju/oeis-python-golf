# A000802

> Maximal number of states in the minimal deterministic finite automaton accepting a language over a binary alphabet consisting of some words of length n.
> — [OEIS A000802](https://oeis.org/A000802)

Offset 0: 1, 2, 4, 7, 11, 19, 34, 50, 82, 146, 274, 529, 785, 1297, 2321, 4369, 8465, 16657, 33041, 65809, …

### Python 3 — 74 bytes

```python
m=1
while[print(sum(2**min(k,t:=2**(m+~k))-(t<=k)for k in range(m)))]:m+=1
```

**The formula**

Champarnaud and Pin (1989) found the largest minimal DFA for a set of
binary words of one length n; the OEIS page states their answer as

a(n) = Σ_{k=0..n} min(2^k, 2^(2^(n−k)) − 1).

A state at depth k is reached by one of the 2^k prefixes of length k and
is fixed by its nonempty set of suffixes of length n − k, so each level
holds at most min(2^k, 2^(2^(n−k)) − 1) states; they showed that every
level can reach its bound at once.

**How it works**

- `m` is n + 1, so `range(m)` is k = 0 … n and `m+~k` = m − 1 − k = n − k:
  `t` is 2^(n−k), the number of suffixes.
- The second term of the min is never built: 2^t − 1 < 2^k exactly when
  t ≤ k, so min(2^k, 2^t − 1) = 2^min(k,t) − [t ≤ k], which is
  `2**min(k,t)-(t<=k)`. Writing `min(2**k,2**2**(n-k)-1)` directly would
  build a 2^n-bit number at k = 0 and stalls before n = 30.
- The walrus binds `t` inside the min, before `(t<=k)` reads it.

**Notes**

- Exact integer arithmetic, correct for every n given the theorem.
- The b-file has 3301 terms (n = 0 to 3300); they all print in about
  25 s on this PC (term n is a sum of n + 1 numbers of up to n bits). The
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000802), CC BY-SA 4.0.
