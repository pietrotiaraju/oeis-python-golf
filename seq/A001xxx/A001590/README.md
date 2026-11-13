# A001590

> Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) with a(0)=0, a(1)=1, a(2)=0.
> — [OEIS A001590](https://oeis.org/A001590)

Offset 0: 0, 1, 0, 1, 2, 3, 6, 11, 20, 37, 68, 125, 230, 423, 778, 1431, …

### Python 3 — 39 bytes

```python
l=0,1,0
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- `l` is a window of three consecutive terms, starting with the data's
  a(0), a(1), a(2) = 0, 1, 0. `a,*l=*l,sum(l)` drops the oldest term
  into `a`, which is printed, and appends the sum of the three, the next
  term. The same template runs [A000073](../../A000xxx/A000073/).

**Notes**

- The three-variable tuple `a=c=0;b=1` / `a,b,c=b,c,a+b+c` is 41 bytes
  ([A000213](../../A000xxx/A000213/) has the cheap start `a=b=c=1`);
  a search over three-variable tuples with short entries, in other
  coordinates and with any of the variables printed, found nothing
  shorter, and no chain of in-place statements has this characteristic
  polynomial at that size.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001590), CC BY-SA 4.0.
