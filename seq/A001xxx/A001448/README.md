# A001448

> a(n) = binomial(4n,2n) or (4*n)!/((2*n)!*(2*n)!).
> — [OEIS A001448](https://oeis.org/A001448)

Offset 0: 1, 6, 70, 924, 12870, 184756, 2704156, 40116600, 601080390, 9075135300, …

### Python 3 — 49 bytes

```python
c=j=1
while[print(c)]:c=c*(16*j*j-4)//j//-~j;j+=2
```

**How it works**

- With c(j) = C(2j, j), c(j+1)/c(j−1) = (4j−2)(4j+2)/(j(j+1)) =
  (16j² − 4)/(j(j+1)), and a(n) = c(2n). So the loop runs j = 1, 3, 5, …
  (j = 2n + 1 after printing a(n)) and steps
  `c=c*(16*j*j-4)//j//-~j`.
- Both divisions are exact: c(j−1)(4j−2)/j = c(j) is an integer, so
  c(j−1)(16j² − 4)/j = c(j)(4j+2) is one, and dividing that by j + 1 gives
  c(j+1). `-~j` is j + 1.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- `math.comb(n,n//2)` stepping n by 4, with its import, is 52 bytes; the
  ratio in n, 2(4n−1)(4n−3)/(n(2n−1)), is longer to write.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001448), CC BY-SA 4.0.
