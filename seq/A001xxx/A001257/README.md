# A001257

> Squares of numbers of rooted trees.
> — [OEIS A001257](https://oeis.org/A001257)

Offset 0: 1, 1, 4, 16, 81, 400, 2304, 13225, 81796, 516961, 3392964, 22714756, 155900196, 1087218729, 7710771721, …

### Python 3 — 90 bytes

```python
r=[n:=0,1]
while[print(r[-1]**2)]:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
```

**How it works**

- The program is the [A000081](../../A000xxx/A000081/) record (rooted
  trees by the Euler transform), but it prints `r[-1]**2`. The newest
  value starts at r(1) = 1, while the original's `r[-n]` starts at
  r(0) = 0. This sequence's offset 0 corresponds to one node.

**Notes**

- The b-file has only 21 terms, and they print at once. The program
  carries on: A000081's own bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001257), CC BY-SA 4.0.
