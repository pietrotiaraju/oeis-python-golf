# A001994

> Expansion of 1/((1-x)*(1-x^2)^2*(1-x^3)*(1-x^4)*(1-x^5)).
> — [OEIS A001994](https://oeis.org/A001994)

Offset 0: 1, 1, 3, 4, 8, 11, 18, 24, 36, 47, 66, 84, 113, 141, 183, 225, 284, 344, 425, …

### Python 3 — 61 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b'	'];print(v)
```

The bytes literal holds 5 raw control bytes (0x0F, 0x09, 0x08, 0x11, 0x15)
that a browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<0f><09><08><11><15>'];print(v)
```

where `<0f>` stands for the single byte 0x0F, and so on.

**How it works**

- **Layers.** The coefficient of xⁿ in 1/((1 − x)(1 − x²)²(1 − x³)(1 − x⁴)(1 − x⁵)) counts the ways to pay n with coins 1, 2, 2′, 3, 4, 5, where 2′ is a second kind of 2. Pennies alone pay any n ≥ 0 in one way,
  A₀(n) = 1. Add the coins c₁, …, c₅ = 3, 2, 2′, 4, 5 one at a time and let Aⱼ(n)
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
  15, 9, 8, 17, 21. All are below 32, so they sit in the bytes literal as raw control
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

- A closed form exists (Hoang Xuan Thanh's in the entry), with a
  (−1)ⁿ·675(n² + 17n) term over 172800; written out it is far longer.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001994), CC BY-SA 4.0.
