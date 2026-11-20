# A001993

> Number of two-rowed partitions of length 3.
> — [OEIS A001993](https://oeis.org/A001993)

Offset 0: 1, 1, 3, 5, 9, 13, 22, 30, 45, 61, 85, 111, 150, 190, 247, 309, 390, 478, 593, …

### Python 3 — 61 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b''];print(v)
```

The bytes literal holds 5 raw control bytes (0x0F, 0x0E, 0x08, 0x07, 0x10)
that a browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<0f><0e><08><07><10>'];print(v)
```

where `<0f>` stands for the single byte 0x0F, and so on.

**How it works**

- **Layers.** The entry gives the generating function 1/((1 − x)(1 − x²)²(1 − x³)²(1 − x⁴)) for these two-rowed partitions (Cayley, MacMahon); its coefficient of xⁿ counts the ways to pay n with coins 1, 2, 2′, 3, 3′, 4, where 2′ and 3′ are second kinds of 2 and 3. All 1001 terms of the b-file agree. Pennies alone pay any n ≥ 0 in one way,
  A₀(n) = 1. Add the coins c₁, …, c₅ = 3, 3′, 2, 2′, 4 one at a time and let Aⱼ(n)
  count the ways with pennies and c₁, …, cⱼ; a way either uses no cⱼ coin
  or uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and a(n) = A₅(n).
  The order of the coins does not change the count.
- **One flat list.** `a` starts with 99 zeros and each pass appends row n:
  A₁(n), …, A₅(n). While row n is built the list still has 99 + 5n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`, so slot k (k = 0…4) of row n − c is 5c − k places before
  the end, `a[-(5c-k)]`; for n < c that index falls into the leading zeros,
  which supply Aⱼ(m) = 0 for m < 0.
- **The offsets.** For k = 0…4 and the coins in this order, 5c − k is
  15, 14, 8, 7, 16. All are below 32, so they sit in the bytes literal as raw control
  bytes; this order keeps 10–13 and 28–30 (line breaks, also for
  `str.splitlines`), the quote 39 and the backslash out of the literal.
  Iterating over a bytes object gives ints, so `i` is the offset itself.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of
  every pass (and is always true); `v:=v+a[-i]` turns v into A₁(n), …,
  A₅(n) in turn and stores each as its slot. The walrus in the
  comprehension binds the outer `v`, so after the row v = a(n), which is
  printed. The template is the one of [A001300](../A001300/) and
  [A001401](../A001401/).
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- A closed form exists (Hoang Xuan Thanh's in the entry), but it carries a
  (−1)ⁿ·(n² + 15n)/256 term and a mod-3 term and is far longer.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001993), CC BY-SA 4.0.
