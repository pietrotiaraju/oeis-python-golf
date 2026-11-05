# A000095

> Number of fixed points of Gamma_0 (n) of type i.
> — [OEIS A000095](https://oeis.org/A000095)

Offset 1: 1, 2, 0, 0, 2, 0, 0, 0, 0, 4, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 4, …

### Python 3 — 57 bytes

```python
n=2
while[print(sum(n-2==x*x%n*2for x in range(n)))]:n+=2
```

**How it works**

- Write k for the index and n = 2k. Then a(k) is the number of residues
  x = 0 … 2k − 1 with x² + 1 ≡ k (mod 2k). This follows from the OEIS
  formula a(k) = 2·A000089(k) − A000089(2k), where A000089(m) counts the
  roots of x² + 1 ≡ 0 (mod m). There are 2·A000089(k) residues mod 2k
  with k | x² + 1, and A000089(2k) of them also have 2k | x² + 1. The
  rest have x² + 1 ≡ k (mod 2k).
- The program counts in steps of 2, so `n` is 2k: `n=2`, `n+=2` and
  `range(n)` run over every residue mod 2k.
- x² + 1 ≡ n/2 (mod n) is the same as x² mod n = n/2 − 1, and n/2 − 1 is
  in 0 … n − 1, so `n-2==x*x%n*2` checks it with integers only. It is
  2 bytes shorter than `(x*x+1)%n*2==n`.
- Check: k = 1 gives x = 0 (1 ≡ 1 mod 2), so a(1) = 1. k = 2 gives x = 1
  and 3 (x² + 1 ≡ 2 mod 4), so a(2) = 2. That is the only even prime
  power that is not 0.
- `while[print(…)]:n+=2` loops forever, because `[None]` is a non-empty
  list. It is a byte shorter than `while 1:print(…);n+=2`.

**Notes**

- The program uses exact integer arithmetic over every residue, so it is
  right for every n. It relies only on the identity
  a(k) = 2·A000089(k) − A000089(2k). That identity follows from the
  multiplicative formula: A000089(2k) = A000089(k) for odd k, and
  A000089(2k) = 0 for even k.
- Each term costs 2k steps. The whole b-file (10000 terms) prints in about
  11 s, and the bar is the whole b-file in 60 s.
- The multiplicative formula (a(n) = 0 if 4 | n, otherwise the product of
  1 + (−1/p) over the primes p dividing n, with (−1/2) = 1) needs a
  factorisation and is much longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000095), CC BY-SA 4.0.
