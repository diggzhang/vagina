# vagina

Procedural Organic ASCII Vagina Art Generator

A small Python package that explores symmetry, curvature, and randomness
to generate organic-looking ASCII forms in the terminal.

Each output is produced procedurally, with no predefined templates.

## Characteristics

- Symmetrical but imperfect  
- Structured but unpredictable  
- Familiar, yet undefined  

## Install

```bash
pip install vagina
````

## Usage

```bash
vagina
```

Generate reproducible output with a fixed seed:

```bash
vagina --seed 42
```

output:

```
# vagina --seed 42
                                   (....\
                                 /...>
                                \.:::/
                                \ <> /
                              \\.~.~~./
                               \..:: ~/
                              \        /
                            \\__________/
                            \_._.:_. _   /
                            \            /
                           \~ ~ ~ ~~.. .  //
                           \              //
                           \.  .  ._ .  _://
                          \\ ~. ~ __~__. ./
                           \\..  .{}   . /
                            \   .  . . ~ //
                            \~.~ .||~ .  /
                           \\            /
                             \ :._. :: :/
                             \........../
                             \\...._ .:/
                             \\ ..().../
                               \__[] _//
                              \\______//
                               \\_._.//
                                \:  _//
                                  (____\
                                    \_____>
                                   /__/
```

Control the size:

```bash
vagina --height 32 --center 40
```

## Python API

```python
from vagina import generate_art

print(generate_art())
print(generate_art(seed=42))
```

## Features

* Procedural generation
* Reproducible output with `--seed`
* Command-line interface
* Importable Python API
