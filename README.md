Road Trip Bingo
===============

This is a Road Trip Bingo generator

Road Trip Bingo is a game where the participants have a 5x5 bingo sheet
of several icons that they cross off when they see them. First one to get a
bingo line wins. Or, especially on longer road trips, print out several of
those sheets (20 or so) and they are all played at the same time. Whoever
gets the most bingos at the end wins. Or make up some other rules, because
it really doesn't matter.

To make things more interesting, make sure they don't all have the same
sheets. That's what the generator is for, it picks a random set of 25 out of
the available icons and spits out a grid that's ready for printing.


Usage
-----

```
$ ./generate.py
DEBUG: Reading from directory icons
DEBUG: Found 47 svg files
DEBUG: Files chosen: icons/toilet.svg, icons/maccas.svg, icons/speedcam.svg
[...]
DEBUG: Processing icons/toilet.svg
DEBUG: Processing icons/maccas.svg
DEBUG: Processing icons/speedcam.svg
DEBUG: Processing icons/ambulance.svg
DEBUG: Processing icons/motorbike.svg
[...]
INFO: Written to output/rtb-0.svg
[...]
```

Use `--help` for information about the generate script.

All files end up in `output` by default. Re-running the script will
overwrite existing files.

License
------

This repository is licensed under the [MIT license](https://spdx.org/licenses/MIT.html):

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice (including the next
> paragraph) shall be included in all copies or substantial portions of the
> Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
