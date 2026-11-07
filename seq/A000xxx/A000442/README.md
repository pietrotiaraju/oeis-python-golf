# A000442

> a(n) = (n!)^3.
> — [OEIS A000442](https://oeis.org/A000442)

Offset 0: 1, 1, 8, 216, 13824, 1728000, 373248000, 128024064000, 65548320768000, 47784725839872000, …

### Python 3 — 34 bytes

```python
a=n=1
while[print(a)]:a*=n**3;n+=1
```

**How it works**

- a holds (k!)³ for the k just printed and n = k+1, so `a*=n**3` makes it
  ((k+1)!)³. The start a = n = 1 prints (0!)³ = 1 and then multiplies by
  1³ for (1!)³ = 1; one chained `a=n=1` is shorter than `a=1;n=0` with the
  increment before the product.
- `while[print(a)]:` prints first in every pass: the one-element list
  holding print's `None` is truthy.

**Notes**

- Same length: a running factorial cubed on output, `f=n=1` /
  `while[print(f**3)]:f*=n;n+=1`. The previous `a=1;n=0` /
  `while[print(a)]:n+=1;a*=n**3` is 36 bytes, and a start-early walrus
  `while[print(a:=a*n**3or 1)]:n+=1` 38.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The b-file has 101 terms (up to
  a(100)); the bar is the whole b-file in 60 s.
- a(609) has 4300 digits and a(610) more, so the int-to-str limit stops
  the printing after a(609).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |
| 2026-11-07 | Python 3 | 34 | `a=n=1` start, multiply after printing |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000442), CC BY-SA 4.0.
