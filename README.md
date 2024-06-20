# AutoFprettify

AutoFprettify is a [Sublime Text](https://www.sublimetext.com/) package
that enables you to auto-format your [Fortran](https://fortran-lang.org/) source code
with [fprettify](https://pypi.org/project/fprettify/).

## Dependencies

You must have `fprettify` installed:

```
pip install fprettify
```

## Installation

Only manual installation is available at present.

1. Download a ZIP file of this repository.
2. Extract the files into a folder named `AutoFprettify` in your [Sublime Text Packages directory](https://www.sublimetext.com/docs/packages.html#locations).

The folder must not have the trailing branch name suffix (e.g., `-main`) that the ZIP file will have by default.

## Usage

The `auto_fprettify` command will only work on on-disk files (not on buffers),
so save your file first.

The default key binding to trigger the `auto_fprettify` command manually is:

```
ctrl+alt+f
```

To have `fprettify` run whenever you save, change your [Package Settings](https://www.sublimetext.com/docs/settings.html):

```
{
    "format_on_save": true,
}
```

To pass command-line options to `fprettify`, set them in your [Package Settings](https://www.sublimetext.com/docs/settings.html):

```
{
    // Set the relative indentation width to 2 and the maximum line length to 80:
    //
    "options": ["-i2", "-l80"],
}
```

### Fortran Source File Detection

This package identifies a file as a Fortran source file if any of the following are true:

- The file extension is one of `.f`, `.for`, `.ftn`, `.f90`, `.f95`, `.f03`, `.fpp`, or their capitalized variants (same as `fprettify`)
- The Sublime Text [scope name](https://www.sublimetext.com/docs/selectors.html) is one of: `source.modern-fortran`, `source.fixedform-fortran`, or `source.fortran`

## License

It's a pretty simple package. Do with it as you like.

Want to add a feature? Pull requests are welcome.
