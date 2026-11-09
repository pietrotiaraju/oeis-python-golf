# A000008

> Number of ways of making change for n cents using coins of 1, 2, 5, 10 cents.
> — [OEIS A000008](https://oeis.org/A000008)

Offset 0: 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 19, 22, 25, 28, …

### Python 3 — 59 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b''];print(v)
```

The bytes literal holds three raw control bytes (0x06, 0x0E and 0x1C) that a
browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<06><0E><1C>'];print(v)
```

where `<06>` stands for the single byte 0x06, and so on. With the bytes
escaped in octal, `b''`, the program is 64 bytes.

**How it works**

- **Layers.** Pennies alone pay any n ≥ 0 in exactly one way: A₀(n) = 1. Add
  the coins c₁, c₂, c₃ = 2, 5, 10 one at a time and let Aⱼ(n) count the ways
  with pennies and c₁, …, cⱼ. A way either uses no cⱼ coin or uses one and
  leaves a way for n − cⱼ, so Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0
  for m < 0, and a(n) = A₃(n).
- **One flat list.** `a` starts with 99 zeros and each pass appends row n:
  A₁(n), A₂(n), A₃(n). While row n is built the list still has 99 + 3n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`. Slot k (k = 0, 1, 2) of row n − c is then 3c − k places
  before the end, at `a[-(3c-k)]`; for n < c the index falls into the
  zeros, which supply Aⱼ(m) = 0 for m < 0.
- **The offsets.** For (k, cⱼ) = (0, 2), (1, 5), (2, 10), 3cⱼ − k is 6, 14,
  28: the bytes 0x06, 0x0E, 0x1C. Iterating over a bytes object gives ints,
  so `i` is the offset itself. Every order of the coins puts one of 28, 29,
  30 (a dime in a row of three slots) into the literal, so a raw control
  byte from 0x1C to 0x1E cannot be avoided.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of
  every pass (and is always true). `v:=v+a[-i]` turns v into A₁(n), A₂(n),
  A₃(n) in turn and stores each as its slot; the walrus in the
  comprehension binds the outer `v`, so after the row v = a(n), which is
  printed.
- The same template is used for [A001301](../../A001xxx/A001301/) and the
  other coin-change pages of that range.

**Notes**

- The previous record (67 bytes) was a closed sum over the number of
  5-cent units t: the 5s and 10s pay 5t in ⌊t/2⌋ + 1 ways and the 1s and 2s
  pay the rest k in ⌊k/2⌋ + 1 ways; with m = n + 12 and j = n + 2 − 5t this
  is

  ```python
  m=12
  while[print(sum((m-j)//10*(j//2)for j in range(m,1,-5)))]:m+=1
  ```

- The OEIS recurrence a(n) = a(n−2) + a(n−5) − a(n−7) + a(n−10) − a(n−12)
  − a(n−15) + a(n−17) + 1, run on a list padded with 17 zeros, is 81 bytes.
- The closed forms on the OEIS entry (Kirchner 2017, Hoang 2025) come out at
  77 bytes or more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 73 | first entry |
| 2026-11-05 | Python 3 | 67 | count down from j = n + 12 in steps of 5 (-6) |
| 2026-11-09 | Python 3 | 59 | layered running sums in one flat list, offsets in a bytes literal (-8) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000008), CC BY-SA 4.0.
