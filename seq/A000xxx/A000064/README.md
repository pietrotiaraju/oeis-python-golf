# A000064

> Partial sums of (unordered) ways of making change for n cents using coins of 1, 2, 5, 10 cents.
> — [OEIS A000064](https://oeis.org/A000064)

Offset 0: 1, 2, 4, 6, 9, 13, 18, 24, 31, 39, 50, 62, 77, 93, 112, 134, 159, …

### Python 3 — 60 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b'%'];print(v)
```

The bytes literal holds three raw control bytes (0x04, 0x07 and 0x12) that a
browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<04><07><12>%'];print(v)
```

where `<04>` stands for the single byte 0x04, and so on. With those bytes
escaped in octal, `b'%'`, the program is 64 bytes.

**How it works**

Summing [A000008](../A000008/) up to n is the same as adding a second kind
of 1-cent coin: a(n) counts the partitions of n into parts 1 (two kinds),
2, 5 and 10, with g.f. 1/((1 − x)²(1 − x²)(1 − x⁵)(1 − x¹⁰)).

- **Layers.** One kind of penny alone pays any n ≥ 0 in exactly one way:
  A₀(n) = 1. Add the coins c₁, …, c₄ = 1 (the second kind), 2, 5, 10 one at
  a time and let Aⱼ(n) count the ways with the first penny and c₁, …, cⱼ.
  A way either uses no cⱼ coin or uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and a(n) = A₄(n).
- **One flat list.** `a` starts with 99 zeros and each pass appends row n:
  A₁(n), …, A₄(n). While row n is built the list still has 99 + 4n entries,
  because `a+=[…]` evaluates the whole comprehension before it extends `a`.
  Slot k (k = 0…3) of row n − c is then 4c − k places before the end, at
  `a[-(4c-k)]`; for n < c the index falls into the zeros, which supply
  Aⱼ(m) = 0 for m < 0.
- **The offsets.** For (k, cⱼ) = (0, 1), (1, 2), (2, 5), (3, 10), 4cⱼ − k is
  4, 7, 18, 37: the bytes 0x04, 0x07, 0x12 and `%`. Iterating over a bytes
  object gives ints, so `i` is the offset itself.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of
  every pass (and is always true). `v:=v+a[-i]` turns v into A₁(n), …,
  A₄(n) in turn and stores each as its slot; the walrus in the
  comprehension binds the outer `v`, so after the row v = a(n), which is
  printed. The same template gives [A000008](../A000008/).

**Notes**

- The previous record (69 bytes) paid 5t cents with nickels and dimes
  in ⌊t/2⌋ + 1 ways and the other k = n − 5t cents with the two pennies and
  the 2s in ⌊(k + 2)²/4⌋ ways; with m = n + 12 and j = k + 2 it is

  ```python
  m=12
  while[print(sum((m-j)//10*(j*j//4)for j in range(m,1,-5)))]:m+=1
  ```

- Each term takes four list reads, so the whole b-file (n ≤ 1000) prints in
  well under a second.
- Another split gives the same length as the previous record: the coins 1, 2, 5 alone pay k cents
  in round((k + 4)²/20) ways ([A000115](https://oeis.org/A000115)), the
  other 1-cent coin and the dimes pay s cents in ⌊s/10⌋ + 1 ways, and
  `m=14` with `(m-j)//10*((j*j+9)//20)for j in range(m)` is also 69 bytes.
- Folding the nickels in as well, the coins 1, 1, 2, 5 pay k cents in
  ⌊(j³ − 31j + 200)/480⌋ ways with j = 2k + 9; summing that over the dimes
  (`m=9`, `range(m,0,-20)`, `m+=2`) is 71 bytes.
- The closed form on the OEIS entry (Tani Akinari, 2014) needs a (−1)ⁿ term
  and a period-5 table, both growing with n, and is over 80 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 69 | first entry |
| 2026-11-09 | Python 3 | 60 | layered running sums in one flat list, offsets in a bytes literal (-9) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000064), CC BY-SA 4.0.
