# A001401

> Number of partitions of n into at most 5 parts.
> — [OEIS A001401](https://oeis.org/A001401)

Offset 0: 1, 1, 2, 3, 5, 7, 10, 13, 18, 23, 30, 37, 47, 57, 70, 84, 101, 119, 141, 164, …

### Python 3 — 60 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b'	'];print(v)
```

The bytes literal holds four raw control bytes (0x14, 0x0F, 0x06 and a tab,
0x09) that a browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<14><0f><06><09>'];print(v)
```

where `<14>` stands for the single byte 0x14, and so on.

**How it works**

- **Layers.** Partitions into at most 5 parts are, by conjugation,
  partitions into parts of size at most 5: ways to pay n with coins
  1, …, 5. Pennies alone pay any n ≥ 0 in one way, A₀(n) = 1. Add the coins
  c₁, …, c₄ = 5, 4, 2, 3 one at a time and let Aⱼ(n) count the ways with
  pennies and c₁, …, cⱼ; a way either uses no cⱼ or uses one and leaves a
  way for n − cⱼ, so Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0,
  and a(n) = A₄(n) (the order of the coins does not change the count).
- **One flat list.** `a` starts with 99 zeros and each pass appends row n:
  A₁(n), …, A₄(n). While row n is built the list still has 99 + 4n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`, so slot k (k = 0…3) of row n − c is 4c − k places before the
  end, `a[-(4c-k)]`; for n < c that index falls into the leading zeros,
  which supply Aⱼ(m) = 0 for m < 0.
- **The offsets.** For (k, cₖ₊₁) = (0, 5), (1, 4), (2, 2), (3, 3), 4c − k is 20, 15, 6, 9. All are
  below 32, so they sit in the bytes literal as raw control bytes (one byte
  each); this order of the coins keeps 10 and 13 (line breaks), 11, 12 and
  28–30 (which `str.splitlines` treats as line breaks) and the quote 39 out
  of the literal. Iterating over a bytes object gives ints, so `i` is the
  offset itself.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true); `v:=v+a[-i]` turns v into A₁(n), …, A₄(n)
  in turn and stores each as its slot. The walrus in the comprehension binds
  the outer `v`, so after the row v = a(n), which is printed.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- A closed form exists (Washington Bomfim's in the entry; with u = 2n + 15
  it is ⌊(u⁴ − 110u² + 360u(u mod 4 − 2) + c)/46080⌋ for a suitable c), but
  written out (c = 15000) it is 66 bytes, 6 more than the template.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001401), CC BY-SA 4.0.
