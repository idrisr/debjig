# debjig

`debjig` is a utility program for learning new libraries. Often times I want to
know what function or method was called when running code. Altering the source
with print and log statement is tedious.

Instead of large alterations to source which can be difficult to undo, `debjib`
provides a simple decorator function `log()` which can decorate any function.

Functions decorated with `log()` will log their names to `std.err` when they are
called. Going back to the original is as simple as removing the `log()`
decorator.
