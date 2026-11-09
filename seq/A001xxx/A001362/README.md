# A001362

> Number of ways of making change for n cents using coins of 1, 2, 4, 10 cents.
> — [OEIS A001362](https://oeis.org/A001362)

Offset 0: 1, 1, 2, 2, 4, 4, 6, 6, 9, 9, 13, 13, 18, 18, 24, 24, 31, 31, 39, 39, 49, …

### Python 3 — 59 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b''];print(v)
```

The bytes literal holds three raw control bytes (0x1E, 0x0B and 0x04) that a browser
does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<1E><0B><04>'];print(v)
```

where `<1E>` stands for the single byte 0x1E, and so on.

**How it works**

- **Layers.** Pennies alone pay any n ≥ 0 in exactly one way: A₀(n) = 1.
  Add the other coins one at a time, c₁, c₂, c₃ = 10, 4, 2, and let Aⱼ(n)
  count the ways with pennies and c₁, …, cⱼ. A way either uses no cⱼ coin or
  uses one and leaves a way for n − cⱼ, so Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ),
  with Aⱼ(m) = 0 for m < 0, and a(n) = A₃(n). This is the generating
  function 1/((1 − x)(1 − x²)(1 − x⁴)(1 − x¹⁰)) taken one factor at a time;
  the order of the coins does not change the count.
- **One flat list.** `a` starts with 99 zeros and each pass appends row n:
  A₁(n), A₂(n), A₃(n). `a+=[…]` evaluates the whole comprehension before it
  extends `a`, so while row n is built the list has 99 + 3n entries, and
  slot k (k = 0, 1, 2) of row n − c sits 3c − k places before the end. For
  (k, cⱼ) = (0, 10), (1, 4), (2, 2) the offsets are 30, 11 and 4, the three
  bytes of the literal (iterating over a bytes object gives ints). For
  n < cⱼ the index falls into the leading zeros, which supply Aⱼ(m) = 0.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of
  every pass (and is always true). `v:=v+a[-i]` turns v into A₁(n), A₂(n),
  A₃(n) in turn and stores each as its slot; the walrus in the
  comprehension binds the outer `v`, so after the row v = a(n), which is
  printed. The same template gives [A000008](../../A000xxx/A000008/) and
  [A001300](../A001300/).

**Notes**

- The generator form of [A001306](../A001306/), which stores the coins
  themselves (`a[-3*c]for c in b'…'`), is 62 bytes here: two bytes for
  `3*`, and the coin 10 needs the escape `\n`. The quasi-polynomial
  ⌊(2n³ + 51n² + 3(−1)ⁿ(n² + 17n) + 373n + 1152)/960⌋ given on the OEIS page
  is longer as a program.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n³/480, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is all of them in 60 s,
  which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001362), CC BY-SA 4.0.
