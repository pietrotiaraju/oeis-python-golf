# A001356

> Dates at fortnightly intervals from Jan 01 in the Julian calendar.
> — [OEIS A001356](https://oeis.org/A001356)

Offset 1: 1, 15, 29, 12, 26, 12, 26, 9, 23, 7, 21, 4, 18, 2, 16, 30, 13, 27, …

### Python 3 — 51 bytes

```python
x=1227
while[print((x%1461//4*5+2)%153//5+1)]:x+=56
```

**How it works**

a(n) is the day of the month of the date 14(n − 1) days after January 1
of a year that follows a Julian leap year (the entry's comment), so n = 1,
2, 3, … are Jan 1, Jan 15, Jan 29, Feb 12, …

- **Days from March 1 of a leap year.** Count D days from March 1 of the
  leap year L before the start. Then the Julian calendar repeats every
  1461 days, and its four years, read from March to February, have
  365, 365, 365 and 366 days: the leap day, Feb 29 of L + 4, is the last
  day of the cycle. January 1 of L + 1 is D = 306 (the days of March to
  December), and term n is D = 306 + 14(n − 1).
- **Day of the March year.** With D = 365y + d (y = 0…3, d the day of its
  March year, 0 for March 1), 4D + 3 = 1461y + (4d + 3 − y), and
  0 ≤ 4d + 3 − y < 1461 for every day of the cycle (d ≤ 364, or d ≤ 365
  when y = 3). So d = ((4D + 3) mod 1461) // 4 for every D, cycle and all.
  The program keeps x = 4D + 3, which starts at 1227 and grows by
  4 · 14 = 56 per term; `x%1461//4` is d.
- **Day of the month.** From March on, the month lengths 31, 30, 31, 30,
  31 repeat with period 153 days in five months, and February comes last,
  so no month is cut short before it ends. The usual month formula is
  m = (5d + 2) // 153 (m = 0 for March); writing 5d + 2 = 153m + s gives
  the day of the month d − (153m + 2) // 5 + 1 = s // 5 + 1, that is
  `(d*5+2)%153//5+1`. Feb 29 is d = 365: s = 152, day 29.
- `while[print(…)]:` prints and loops forever (the list is never empty).

**Notes**

- Exact integer arithmetic on numbers below 1461 · 4, correct for every n;
  the sequence has period 1461, and the b-file (10000 terms) covers it
  several times.
- With `datetime` (proleptic Gregorian, whose years 1 to 4 have the
  Julian pattern) it is 74 bytes: `from datetime import*` / `n=1` /
  `while[print(date.fromordinal(n).day)]:n=n%1461+14`, where `n%1461+14`
  steps the ordinal by 14 modulo 1461 without leaving years 1 to 5.
- The bar is the whole b-file (10000 terms) in 60 s, which takes a
  fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001356), CC BY-SA 4.0.
