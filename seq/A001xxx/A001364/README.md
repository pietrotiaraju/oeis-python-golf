# A001364

> Number of ways of making change for n cents using coins of 1, 2, 4, 12, 24, 48, 96, 120 cents (based on English coinage of 1939).
> — [OEIS A001364](https://oeis.org/A001364)

Offset 0: 1, 1, 2, 2, 4, 4, 6, 6, 9, 9, 12, 12, 17, 17, 22, 22, 29, 29, 36, 36, 45, …

### Python 3 — 66 bytes

```python
a=[0]*999
while v:=1:a+=(v:=v+a[-7*c]for c in b'0`x');print(v)
```

The bytes literal holds four raw control bytes (0x02, 0x04, 0x0C and 0x18) that a browser
does not show. Byte for byte, the second line is

```text
while v:=1:a+=(v:=v+a[-7*c]for c in b'<02><04><0C><18>0`x');print(v)
```

where `<02>` stands for the single byte 0x02, and so on.

**How it works**

- **Layers.** The coins are the farthing (1), halfpenny (2), penny (4),
  threepence (12), sixpence (24), shilling (48), florin (96) and half-crown
  (120), counted in farthings. Farthings alone pay any n ≥ 0 in one way:
  A₀(n) = 1. Add the other seven coins c₁, …, c₇ one at a time and let
  Aⱼ(n) count the ways with farthings and c₁, …, cⱼ. A way either uses no
  cⱼ coin or uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and a(n) = A₇(n),
  the coefficient of xⁿ in the generating function on the OEIS page.
- **One flat list, read while it grows.** `a` starts with 999 zeros and each
  pass appends row n: A₁(n), …, A₇(n). `a+=` with a generator extends `a`
  one item at a time (CPython's `list.extend` appends each item as soon as
  the generator yields it), and the generator reads `a` in between. When
  Aⱼ(n) is computed, `a` holds 999 + 7n + (j − 1) entries and Aⱼ(n − cⱼ) is
  entry 999 + 7(n − cⱼ) + (j − 1), exactly 7cⱼ from the end: `a[-7*c]`.
  For n < cⱼ that entry is one of the leading zeros (7cⱼ ≤ 840 < 999).
- **The coins.** Iterating over a bytes object gives ints, so the literal
  holds the coins themselves: 0x02, 0x04, 0x0C, 0x18, `0`, `` ` `` and `x`
  are 2, 4, 12, 24, 48, 96 and 120.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true). `v:=v+a[-7*c]` turns v into A₁(n), …, A₇(n) in
  turn and yields each, which stores it as its slot; a walrus inside a
  generator binds the outer `v`, so after the row v = a(n), which is
  printed. Same template as [A001306](../A001306/).

**Notes**

- The list-comprehension form of [A001300](../A001300/) reads `a` before any
  of the row is stored, so it would need the offsets 7cⱼ − k, up to 840:
  they do not fit in a bytes literal.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁷, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is all of them in 60 s,
  which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001364), CC BY-SA 4.0.
