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
