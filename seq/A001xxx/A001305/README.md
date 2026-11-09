# A001305

> Expansion of 1/((1-x)^2*(1-x^2)*(1-x^5)*(1-x^10)*(1-x^20)).
> — [OEIS A001305](https://oeis.org/A001305)

Offset 0: 1, 2, 4, 6, 9, 13, 18, 24, 31, 39, 50, 62, 77, 93, 112, 134, 159, 187, 218, 252, 293, …

### Python 3 — 61 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b'/`'];print(v)
```

The bytes literal holds three raw control bytes (0x05, 0x18 and 0x08) that a
browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<05><18><08>/`'];print(v)
```

where `<05>` stands for the single byte 0x05, and so on. With those three
bytes escaped in octal, `` b'\5\30\10/`' ``, the program is 66 bytes.

**How it works**

- **Layers.** a(n) counts the ways to write n = Σ cⱼxⱼ with xⱼ ≥ 0 and parts
  1, 1, 2, 5, 10, 20 (one factor 1/(1−x^c) each). With the first 1 alone,
  n ≥ 0 is reached in exactly one way: A₀(n) = 1. Add the other parts one at
  a time, in the order c₁, …, c₅ = 1, 5, 2, 10, 20 (the order of the factors
  does not matter), and let Aⱼ(n) count the ways with the first j + 1 parts.
  A way either has xⱼ = 0 or has xⱼ ≥ 1 and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and a(n) = A₅(n).
- **One flat list.** `a` starts with 99 zeros, and each pass appends row n:
  A₁(n), …, A₅(n). While row n is being built the list still has 99 + 5n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`. Slot k (k = 0…4) of row n − c then sits 5c − k places before
  the end, at `a[-(5c-k)]`; for n < c that index falls into the padding,
  which supplies Aⱼ(m) = 0 for m < 0 (the largest offset is 96).
- **The offsets.** For the slots (k, cⱼ) = (0, 1), (1, 5), (2, 2), (3, 10),
  (4, 20), 5cⱼ − k is 5, 24, 8, 47, 96: the bytes 0x05, 0x18, 0x08, `/` and
  `` ` ``. Iterating over a bytes object gives ints, so `i` is the offset
  itself. With 20 last its offset stays under 100, so 99 zeros of padding
  are enough, and 2 goes third so that its offset is not 10 (a line break)
  or 9 (a tab, which would be legal but invisible).
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true). In the comprehension `v:=v+a[-i]` turns v into
  A₁(n), …, A₅(n) in turn, and each value is stored as its slot; a walrus
  inside a comprehension binds the outer `v`, so after the row v is
  A₅(n) = a(n), which is printed.

**Notes**

- Same template as [A001301](../A001301/). A closed sum over the 10- and
  20-cent coins, weighting the cubic of [A001304](../A001304/) (the first
  four factors) by ⌊r/2⌋ + 1, `m=49` /
  `while[print(sum((m-s)//40*((s**3-31*s+270)//480)for s in range(m,-9,-20)))]:m+=2`,
  is 85 bytes.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁵/240000, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001305), CC BY-SA 4.0.
