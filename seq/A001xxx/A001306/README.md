# A001306

> Number of ways of making change for n cents using coins of 1, 5, 10, 20, 50, 100 cents.
> — [OEIS A001306](https://oeis.org/A001306)

Offset 0: 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 10, …

### Python 3 — 67 bytes

```python
a=[0]*999
while v:=1:a+=[v:=v+a[-ord(i)]for i in'1b÷ǰ'];print(v)
```

The string holds one raw control character (U+0019) that a browser does not
show, and two characters above 127, `÷` (U+00F7) and `ǰ` (U+01F0), which are
2 bytes each in UTF-8. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-ord(i)]for i in'<19>1b÷ǰ'];print(v)
```

where `<19>` stands for the single byte 0x19. With it escaped,
`'\x191b÷ǰ'` (an octal `\31` would swallow the `1` after it), the program is
70 bytes.

**How it works**

- **Layers.** Pennies alone pay any n ≥ 0 in exactly one way: A₀(n) = 1. Add
  the other coins one at a time, c₁, …, c₅ = 5, 10, 20, 50, 100, and let
  Aⱼ(n) count the ways with pennies and c₁, …, cⱼ. A way either uses no cⱼ
  coin or uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and a(n) = A₅(n).
- **One flat list.** `a` starts with 999 zeros, and each pass appends row n:
  A₁(n), …, A₅(n). While row n is being built the list still has 999 + 5n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`. Slot k (k = 0…4) of row n − c then sits 5c − k places before
  the end, at `a[-(5c-k)]`; for n < c that index falls into the padding,
  which supplies Aⱼ(m) = 0 for m < 0 (the largest offset is 496).
- **The offsets.** 5cⱼ − k is 25, 49, 98, 247, 496. The last one does not fit
  in a byte, so the offsets are the code points of a `str`, read with `ord`:
  U+0019, `1`, `b`, `÷` and `ǰ`.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true). In the comprehension `v:=v+a[-ord(i)]` turns v
  into A₁(n), …, A₅(n) in turn, and each value is stored as its slot; a
  walrus inside a comprehension binds the outer `v`, so after the row v is
  A₅(n) = a(n), which is printed.

**Notes**

- This is the template of [A001301](../A001301/), which reads its offsets
  from a bytes literal; here 496 is too big for one, so `ord` (5 bytes) is
  the price.
- Pennies pay any remainder, so a(n) = A001307(⌊n/5⌋), where
  [A001307](../A001307/) counts the same coins in units of 5 cents (with an
  extra 1 for the slack). Its 61-byte program with the print repeated,
  `exec('print(v);'*5)`, is 72 bytes. Keeping the coins themselves in a bytes
  literal and appending one slot at a time, so that every offset is 5c, is 69
  as a comprehension, `[a:=a+[v:=v+a[-5*c]]for c in b'…']`, and 70 as a
  `for` loop.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁵/600000000, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001306), CC BY-SA 4.0.
