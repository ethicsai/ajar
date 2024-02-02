# AJAR

> Author: Rémy Chaput  
> (original idea and code by Benoît Alcaraz, Rémy Chaput, Christopher Leturc,
> and Olivier Boissier)


## Description

**AJAR** (Argumentation-based Judging Agents framework for ethical Reinforcement
Learning) is a Python library to judge the behaviours of Reinforcement Learning
(RL) agents, based on moral values that are represented as argumentation graphs.


## Quick usage

Clone this repository or install it through 
`pip install git+https://github.com/ethicsai/ajar.git`, then open a Python
shell (3.7+), and execute the following code:

```python
from ajar import AFDM, JudgingAgent, Argument, judgment

decision = 'moral'
afdm = AFDM()

afdm.add_argument(Argument(
    'argument_name',
    'An argument description',
    support=[decision]
))
afdm.add_argument(Argument(
    'other_argument',
    'Another argument',
    counter=[decision]
))
afdm.add_attack_relation('argument_name', 'other_argument')

judge = JudgingAgent('My moral value', afdm, judgment.j_simple)

reward = judge.judge(situation={}, decision=decision)
```

This will create a new graph (`afdm`), populate it with 2 arguments
(`argument_name` and `other_argument`), as well as an attack from the first
argument onto the second. Finally, we create a `judge` that represents a given
moral value by using this `afdm`. The `judge` can then be used to judge a
situation by calling `judge.judge({}, decision)`. It will return a scalar
number that corresponds to the extent that the given situation respects the
moral value.

To go further, please refer to the [documentation].


## Versioning

This project follows the [Semver] (Semantic Versioning): all versions respect
the `<major>.<minor>.<patch>` format. The `patch` number is increased when a
bugfix is released. The `minor` number is increased when new features are added
that *do not* break the code public API, i.e., it is compatible with the
previous minor version. Finally, the `major` number is increased when a breaking
change is introduced; an important distinction is that such a change may not
be "important" in terms of lines of code, or number of features modified.
Simply changing a function's return type can be considered a breaking change
in the public API, and thus worthy of a "major" update.


## Community

The community guidelines are available in the [CONTRIBUTING.md](CONTRIBUTING.md)
file; you can find a (short) summary below.

### Getting support

If you have a question (something that is not clear, how to get a specific
result, ...), do not hesitate to create a new [Discussion under the Q&A category](https://github.com/ethicsai/ajar/discussions/new?category=q-a).

Please do *not* use the issue tracker for support, to avoid cluttering it.

### Report a bug

If you found a bug (an error raised, or something not working as expected), you
can report it on the [Issue Tracker](https://github.com/ethicsai/ajar/issues/new).

Please try to be as *precise* as possible.

### Contributing

We very much welcome and appreciate contributions!

For fixing bugs, or improving the documentation, you can create a
[Pull Request](https://github.com/ethicsai/ajar/pulls).

New features are also welcome, but larger features should be discussed first in
a new [Discussion under the Ideas category](https://github.com/ethicsai/ajar/discussions/new?category=ideas).

All ideas, suggestions, and requests are also welcome for discussion.


## License

The source code is licensed under the [MIT License] (see also the [LICENSE]
file in this repository).


## Citation

If you use this package in your research, please cite the corresponding paper:

> Benoît Alcaraz, Olivier Boissier, Rémy Chaput, and Christopher Leturc. 2023.
> AJAR: An Argumentation-based Judging Agents Framework for Ethical Reinforcement
> Learning. In Proceedings of the 2023 International Conference on Autonomous
> Agents and Multiagent Systems (AAMAS '23). International Foundation for
> Autonomous Agents and Multiagent Systems, Richland, SC, 2427–2429.
> DOI: 10.5555/3545946.3598956

```bibtex
@inproceedings{10.5555/3545946.3598956,
    author = {Alcaraz, Beno\^{\i}t and Boissier, Olivier and Chaput, R\'{e}my and Leturc, Christopher},
    title = {AJAR: An Argumentation-Based Judging Agents Framework for Ethical Reinforcement Learning},
    year = {2023},
    isbn = {9781450394321},
    publisher = {International Foundation for Autonomous Agents and Multiagent Systems},
    address = {Richland, SC},
    booktitle = {Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems},
    pages = {2427–2429},
    numpages = {3},
    location = {London, United Kingdom},
    series = {AAMAS '23}
}
```

[documentation]: https://ethicsai.github.io/ajar/
[Semver]: https://semver.org/
[MIT License]: https://choosealicense.com/licenses/mit/
[LICENSE]: LICENSE
