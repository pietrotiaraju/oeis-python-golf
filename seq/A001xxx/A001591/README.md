# A001591

> Pentanacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) + a(n-5), a(0)=a(1)=a(2)=a(3)=0, a(4)=1.
> — [OEIS A001591](https://oeis.org/A001591)

Offset 0: 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 31, 61, 120, 236, 464, 912, 1793, …

### Python 3 — 43 bytes

```python
l=0,0,0,0,1
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- `l` is a window of five consecutive terms, starting with the data's
  a(0), …, a(4) = 0, 0, 0, 0, 1. `a,*l=*l,sum(l)` drops the oldest term
  into `a`, which is printed, and appends the sum of the five, the next
  term (the template of [A000078](../../A000xxx/A000078/)).

**Notes**

- `l=[0]*4+[1]` is the same length as `l=0,0,0,0,1`. The form
  a(n) = 2a(n−1) − a(n−6) needs six seeds and is longer.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001591), CC BY-SA 4.0.
