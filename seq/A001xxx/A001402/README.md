# A001402

> Number of partitions of n into at most 6 parts.
> — [OEIS A001402](https://oeis.org/A001402)

Offset 0: 1, 1, 2, 3, 5, 7, 11, 14, 20, 26, 35, 44, 58, 71, 90, 110, 136, 163, 199, 235, …

### Python 3 — 61 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b'	'];print(v)
```

The bytes literal holds five raw control bytes (0x0F, a tab 0x09, 0x17, 0x1B
and 0x10) that a browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<0f><09><17><1b><10>'];print(v)
```

where `<0f>` stands for the single byte 0x0F, and so on.

**How it works**

- **Layers.** Partitions into at most 6 parts are, by conjugation,
  partitions into parts of size at most 6: ways to pay n with coins
  1, …, 6. Pennies alone pay any n ≥ 0 in one way, A₀(n) = 1. Add the coins
  c₁, …, c₅ = 3, 2, 5, 6, 4 one at a time and let Aⱼ(n) count the ways with
  pennies and c₁, …, cⱼ; a way either uses no cⱼ or uses one and leaves a
  way for n − cⱼ, so Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0,
  and a(n) = A₅(n) (the order of the coins does not change the count).
- **One flat list.** `a` starts with 99 zeros and each pass appends row n:
  A₁(n), …, A₅(n). While row n is built the list still has 99 + 5n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`, so slot k (k = 0…4) of row n − c is 5c − k places before the
  end, `a[-(5c-k)]`; for n < c that index falls into the leading zeros,
  which supply Aⱼ(m) = 0 for m < 0.
- **The offsets.** For (k, cₖ₊₁) = (0, 3), (1, 2), (2, 5), (3, 6), (4, 4), 5c − k is 15, 9, 23, 27, 16. All are
  below 32, so they sit in the bytes literal as raw control bytes (one byte
  each); this order of the coins keeps 10 and 13 (line breaks), 11, 12 and
  28–30 (which `str.splitlines` treats as line breaks) and the quote 39 out
  of the literal. Iterating over a bytes object gives ints, so `i` is the
  offset itself.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true); `v:=v+a[-i]` turns v into A₁(n), …, A₅(n)
  in turn and stores each as its slot. The walrus in the comprehension binds
  the outer `v`, so after the row v = a(n), which is printed.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- Same template as [A001401](../A001401/) with one more coin; the quasi-
  polynomial closed forms in the entry are much longer.
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001402), CC BY-SA 4.0.
