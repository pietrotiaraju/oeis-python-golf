# A000202

> a(8i+j) = 13i + a(j), where 1<=j<=8.
> — [OEIS A000202](https://oeis.org/A000202)

Offset 1: 1, 3, 4, 6, 8, 9, 11, 12, 14, 16, …

### Python 3 — 29 bytes

```python
n=12
while[print(n//8)]:n+=13
```

**How it works**

- a(n) = ⌊(13n − 1)/8⌋ (Schoenfield's formula in the entry). It gives
  1, 3, 4, 6, 8, 9, 11, 12 for n = 1…8, and adding 8 to n adds exactly 13,
  so it satisfies a(8i + j) = 13i + a(j).
- `n` holds 13k − 1 for the k-th term: it starts at 12 and grows by 13, so
  each term is just `n//8`. No multiplication and no separate counter.
- `while[print(…)]:` runs the print in the loop test: the list `[None]` is
  non-empty, hence true, and the body only steps `n`. One byte under
  `while 1:print(n//8);n+=13`.

**Notes**

- Integer arithmetic only, so it is correct for every n. It prints the
  whole b-file (10000 terms) at once; the bar is the whole b-file in 60 s.
- 13/8 is a convergent of φ, and the sequence matches the lower Wythoff
  sequence ⌊nφ⌋ ([A000201](../A000201/)) up to n = 20; they first differ at
  n = 21 (34 against 33).
- The direct form `n=1` / `while[print((13*n-1)//8)]:n+=1` is 34 bytes;
  `n>>3` in place of `n//8` ties.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000202), CC BY-SA 4.0.
