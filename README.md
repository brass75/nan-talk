# This is not the NaN you are looking for

Alternate title: "NaN - More than Not a Number"

- Python oddities concerning NaN
- Live demo a dict that allows use of NaN as a key the way it would be intuitively, so that all NaN values are treated as one.
- Live demo a Counter that counts how many occurences of NaN exist

## Questions

- What about `copy.copy`?

## Description

Have you ever wondered about `float('NaN')`? What it is? What you can do with it? What you
shouldn't do with it? Let's take some time and explore this Not a Number and what it does
(and doesn't do) in Python.

## Outline

- Introduction. 3 minutes
  - Who am I?
  - What am I going to talk about?
  - What led me to write this talk?
- Introducing `NaN`. 3 minutes
  - What is `NaN`?
  - What purpose does `NaN` serve?
  - The differences beteween `float('nan')`, `numpy.nan`, and `math.nan`.
  - How we can tell if a "numeric" value is NaN.
- What makes `NaN` so unique? 5 minutes
  - No 2 instances of `NaN` are the same.
  - All instances of `NaN` have the same `repr`: "nan"
  - `NaN` is not equal to anything, not even itself.
  - `NaN` can be hashed but each instance of `NaN` will have a different hash.
    - A set can contain multiple instances of `NaN`.
    - A dictionary can have multiple `NaN` keys, but good luck accessing the data.
    - If you have an `Iterable` with multiple instances of `NaN` and create a `Counter` from it, each
instance will appear with a count of 1.
- Creating a Pythonic `dict` that can only have one `NaN`. 12 minutes
  - Do a code walkthrough and live demo of a Python subclass of `dict` that can only have one instance of `NaN`.
    - Show how I created the new version of `dict`.
    - Simple live demo showing that we can use `float('nan')` as a dict key. In a regular `dict` it will give a `KeyError` when
attempting to retrieve it; with the new version of `dict` it will work as expected.
  - Do a code walkthrough and live demo of a Python `Counter` class that will count how many instances of `NaN` are in it.
    - Show how I created a `Counter` class that will count all instances of `NaN`.
    - Live demo showing the behaviour of `collections.Counter` and the new `Counter` class.
- Conclusion. 2 minutes
  - Quick recap of what was discussed.
  - Where to find the talk slides.
  - Where to find me.

## Things I've found

```python
>>> float('nan') ** 0
1.0
>>> float('nan') > 1
False
>>> float('nan') < 1
False
>>> float('nan') == 1
False
>>> float('nan') != 1
True
>>>> float('inf') - float('inf')
nan
>>>> f'ba{1e234567 - 1e765432}as'
'bananas'
```

```py
import struct
float_bytes = b"\xaa\xbb\xcc\xdd\xff\xff\xff\xff"
val = struct.unpack("d", float_bytes)[0]
print(val)
print(struct.pack("d", val))
```

In a single precision floating point number (32 bit) there are 2^24 - 2 potential NaN values.

Potential improvements for NaNDict:

- Different types of nans are distinct.
- Perserve the original supplied nan (maybe you do and check_key() does the coalescing).
- A dunder hook for hypothetical future other weird ass values with rogue behaviour like nan.
- An extensive test and performance suite.
- Accept any kind of object for the membership test.
- Accepting unhashable values.

`json` parsing in Python doesn't handle NaN properly.
[pydis](https://discord.com/channels/267624335836053506/267624335836053506/1517687138274119741)


## Quotes

NaN is a lot like infinity in that people want to treat it as a number but It's Not and trying to do that will only lead to surprise and disappointment. - Luna Celste

NaN is a wild land governed by laws both alien and arcane - Luna Celeste

## References

<https://xkcd.com/851/>

<https://brassnet.biz/blog/nan-is-weird.html>

<https://github.com/python/cpython/issues/87641>

<https://twit.social/@brass75/116168712645625711>

<https://discuss.python.org/t/question-about-float-nan/106378>

<https://en.wikipedia.org/wiki/NaN>
