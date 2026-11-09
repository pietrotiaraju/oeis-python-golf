# A001219

> Triangular numbers of form a*(a+1)*(a+2).
> — [OEIS A001219](https://oeis.org/A001219)

Offset 1: 0, 6, 120, 210, 990, 185136, 258474216 (finite: this is the whole sequence)

### Python 3 — 45 bytes

```python
print("""0
6
120
210
990
185136
258474216""")
```

**How it works**

- The sequence is finite and these seven numbers are all of it: they are
  the only triangular numbers t(t+1)/2 that are products a(a+1)(a+2) of
  three consecutive integers. This is a theorem (S. P. Mohanty, *Which
  triangular numbers are products of three consecutive integers?*, Acta
  Math. Hungar. 58 (1991) 31–36; see also Guy, *Unsolved Problems in
  Number Theory*, D3), and the OEIS entry is keyword `fini,full`.
- So the shortest program prints the list. As a check, each term is
  a(a+1)(a+2) = t(t+1)/2 for (a, t) = (0, 0), (1, 3), (4, 15), (5, 20),
  (9, 44), (56, 608), (636, 22736).
- A triple-quoted string holds real line breaks, one byte each instead of
  the two of `
`: 45 bytes against 47 for `print(…,sep='
')`.

**Notes**

- The program ends after the last term, which is the end of the
  sequence (rule 2: it prints every term of the b-file).
- A search cannot stop by itself without the theorem's bound, and with it
  (a ≤ 636) it is longer: `for a in range(637):` plus a triangularity test
  is about 58 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001219), CC BY-SA 4.0.
