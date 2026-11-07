# A000453

> Stirling numbers of the second kind, S(n,4).
> — [OEIS A000453](https://oeis.org/A000453)

Offset 4: 1, 10, 65, 350, 1701, 7770, 34105, 145750, 611501, 2532530, …

### Python 3 — 45 bytes

```python
a=b=c=1
while[print(a)]:c-=~c;b=3*b+c;a=4*a+b
```

**How it works**

- S(n, k) counts the partitions of n labelled elements into k blocks. The
  element n + 1 either joins one of the k blocks of a partition of n
  elements or forms a block of its own, so S(n+1, k) = k·S(n, k) +
  S(n, k−1), with S(n, 1) = 1.
- The three variables run along a staggered diagonal: after t passes,
  c = S(t+2, 2), b = S(t+3, 3) and a = S(t+4, 4). With the update order c,
  b, a, each line reads the value just computed on the line before:
  c ← 2c + 1 is S(t+3, 2) = 2·S(t+2, 2) + S(t+2, 1), then b ← 3b + c is
  S(t+4, 3) = 3·S(t+3, 3) + S(t+3, 2), and a ← 4a + b is
  S(t+5, 4) = 4·S(t+4, 4) + S(t+4, 3). The multipliers are constants, so
  no counter is needed.
- The start a = b = c = 1 is S(4, 4) = S(3, 3) = S(2, 2) = 1, so the first
  print is a(4) = 1.
- `c-=~c` is c − (−c − 1) = 2c + 1, two bytes under `c=2*c+1`.

**Notes**

- Other versions that print the same terms:
  - inclusion–exclusion split into two floors,
    `n=4` / `while[print((2**n+6<<n)//24-3**n//6)]:n+=1`: 46 bytes. Here
    `2**n+6<<n` is 4ⁿ + 6·2ⁿ = 24·S(n, 4) + 4·3ⁿ + 4, and since 3ⁿ ≡ 3
    (mod 6) for n ≥ 1, ⌊(4ⁿ + 6·2ⁿ)/24⌋ = S(n, 4) + (3ⁿ − 3)/6 =
    S(n, 4) + ⌊3ⁿ/6⌋;
  - the single division `(4**n-4*3**n+6*2**n)//24` (the −4 of 24·S(n, 4) =
    4ⁿ − 4·3ⁿ + 6·2ⁿ − 4 can go, it is below 24 and the rest is a multiple
    of 24): 47 bytes in the same loop, 50 with `while 1:` and the −4.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 197 terms print in 0.06 s here. The b-file has 197 terms (up
  to a(200)); the bar is the whole b-file in 60 s.
- S(n, 4) is close to 4ⁿ/24, so a(7145) is the first term with more than
  4300 digits and printing stops there (after about 1.5 s).
- [A000392](../A000392/) is S(n, 3) and [A000481](../A000481/) is S(n, 5),
  the same staggered loop with one variable more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-07 | Python 3 | 45 | staggered diagonal of the Stirling triangle, `c-=~c` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000453), CC BY-SA 4.0.
