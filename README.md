# debjig

`debjig` is a utility program for learning new libraries. Often times I want to
know what function or method was called when running code. Altering the source
with print and log statement is tedious.

Instead of large alterations to source which can be difficult to undo, `debjib`
provides a simple decorator function `log()` which can decorate any function.

Functions decorated with `log()` will log their names to `sys.stderr` when they are
called. Going back to the original is as simple as removing the `log()`
decorator.

## FAQ

1. Where the heck does `debjig` get its name from?

> It's a portmanteua of debug and jig. When working with one's hands, one of the
most important abilities you can have is to make custom tools for each job, aka
a jig. This package is a jig to help exploring new code.
