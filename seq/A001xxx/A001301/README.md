# A001301

> Number of ways of making change for n cents using coins of 1, 2, 5, 10, 25 cents.
> — [OEIS A001301](https://oeis.org/A001301)

Offset 0: 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 19, 22, 25, 28, 31, 34, 40, …

### Python 3 — 60 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b'&a'];print(v)
```

The bytes literal holds two raw control bytes (0x08 and 0x13) that a browser
does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<08><13>&a'];print(v)
```

where `<08>` stands for the single byte 0x08, and so on. With those two bytes
escaped in octal, `b'\10\23&a'`, the program is 64 bytes.

**How it works**

- **Layers.** Pennies alone pay any n ≥ 0 in exactly one way: A₀(n) = 1. Add
  the other coins one at a time, c₁, c₂, c₃, c₄ = 2, 5, 10, 25, and let Aⱼ(n)
  count the ways with pennies and c₁, …, cⱼ. A way either uses no cⱼ coin or
  uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0. Then
  a(n) = A₄(n): this is the generating function
  1/((1−x)(1−x²)(1−x⁵)(1−x¹⁰)(1−x²⁵)) built one factor at a time.
- **One flat list.** `a` starts with 99 zeros, and each pass appends row n:
  A₁(n), A₂(n), A₃(n), A₄(n). While row n is being built the list still has
  99 + 4n entries, because `a+=[…]` evaluates the whole comprehension before
  it extends `a`. Slot k (k = 0…3) of row n − c then sits 4c − k places
  before the end, at `a[-(4c-k)]`. For n < c that index falls into the
  padding, which supplies Aⱼ(m) = 0 for m < 0: the largest offset is 97 and
  there are 99 zeros.
- **The offsets.** For the slots (k, cⱼ) = (0, 2), (1, 5), (2, 10), (3, 25),
  4cⱼ − k is 8, 19, 38, 97: the bytes 0x08, 0x13, `&` and `a`. Iterating over
  a bytes object gives ints, so `i` is the offset itself.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true). In the comprehension `v:=v+a[-i]` turns v into
  A₁(n), A₂(n), A₃(n), A₄(n) in turn, and each value is stored as its slot;
  a walrus inside a comprehension binds the outer `v`, so after the row v is
  A₄(n) = a(n), which is printed.

**Notes**

- The same list with the offsets as a tuple, `for i in(-8,-19,-38,-97)` and
  `a[i]`, is 67 bytes. Appending one entry at a time, so that every layer reads
  `a[-5*c]` and the predecessor `a[-1]` (with an explicit `a+=1,` for the
  penny layer), is 77.
- A closed sum in the style of [A000008](../../A000xxx/A000008/) is 77 bytes:
  `m=22` / `while[print(sum(((m-j)**2+250)//500*(j//2)for j in range(m,1,-5)))]:m+=1`.
  With r = (m − j)/5 it weights ⌊j/2⌋ (pennies and 2-cent coins) by
  round(r²/20), the number of ways to make 5(r − 4) cents from 5, 10 and 25
  ([A000115](https://oeis.org/A000115)).
  Unlike [A001299](../A001299/), no single polynomial P gives a(n) = ⌊P(n)⌋:
  the generating function has a double pole at −1 and triple poles at the
  primitive 5th roots of unity, so the periodic part of a(n) is unbounded.
- Reading a(n) off the generating function at x = 1/B as one big integer,
  `(B:=4<<n)**(n+43)//(B-1)//(B*B-1)//(B**5-1)//(B**10-1)//(B**25-1)%B`, is
  90 bytes and far slower (about 930 terms in 20 s).
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁴/60000, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001301), CC BY-SA 4.0.
