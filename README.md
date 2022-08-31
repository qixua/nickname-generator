# Nickname Generator

You can input the length, and the starting letter(s) of the nickname and you get 21 randomly selected nicknames.

## Table of Contents
- [Installation](https://github.com/qixua/nickname-generator#installation)
- [Usage](https://github.com/qixua/nickname-generator#usage)
- [Stuff I may add in the future](https://github.com/qixua/nickname-generator#stuff-i-may-add-in-the-future)
- [License](https://github.com/qixua/nickname-generator#license)

## Installation
You can install Nickname Generator by:

### Cloning the repository (all platforms)

Make sure you have git and python installed.

Run this to clone the repository:

```
% git clone https://github.com/qixua/nickname-generator/
```

### wget (unix-like operating systems)
Get the source file:
```
% wget https://raw.githubusercontent.com/qixua/nickname-generator/master/script.py
```

Read the Usage section to understand how to use the Nickname Generator.

## Usage

Run this to start the program:

```
% python3 script.py
```

**If you cloned the repository** instead of doing `wget`,

```
cd nickname-generator
```

run this first.

Once started, the program will ask you for length.

```
length :: 
```

Write the length as an integer.

```
length :: 6
```

And it will ask you for the starting letter(s)

```
nickname start :: 
```

Write it normally.

```
nickname start :: ae
```

Now press enter, and:

```

            nickname 0
            ------
            aetyao
            ------

            nickname 1
            ------
            aeccrn
            ------

            nickname 2
            ------
            aebysn
            ------

            nickname 3
            ------
            aelwto
            ------

            .
            .
            .
        up to idx 20 
        (it's 0-based so,\
         21 nicknames in total)
```

Copy what you like, or rerun the program to try different stuff.

## Stuff I may add in the future
- Parameter that lets you save the nicknames in an output file.
- Parameter that lets you tweak the amount of nicknames outputted
- Ability to copy the nickname in a given index
- Parameter that lets you tweak the ending letter(s)

## License
The repository qixua/nickname-generator and all of its source code is licensed by the license: [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)