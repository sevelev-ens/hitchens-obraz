---
layout: page
title: "Hitchens-Obraz"
---

An [Obraz](https://obraz.pirx.ru/) port of [Hitchens](https://github.com/patdryburgh/hitchens), a [Jekyll](http://jekyllrb.com) theme. Uses [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) as template engine.

## Demo [hitchens-obraz.netlify.app](https://hitchens-obraz.netlify.app/)

**Data** The data files from *`_data`* have beed moved to *`_config.yml`*.

**Sass** templates have been rewritten with Jinja's *`include`* syntax and put into *`_include/sass`*, the variables are set in *`assets/css/main.css`*.

**PyYaml** Obraz seems to be affected by some breaking changes introduced in PyYaml between the versions *`5.3.1`* and *`6.0`*. If you have an error *`Error: load() missing 1 required positional argument: 'Loader`*, downgrade PyYaml.

**Netlify** If you deploy to Netlify, make sure to set build command to *`pip install pyyaml==5.3.1 obraz ; obraz build`* and output folder to *`_site`*.

**Static files** Some static files do not end up in the generated output, for example *`/assets/images/divider.svg`* does not appear at [*`https://hitchens-obraz.netlify.app/assets/images/divider.svg`*](https://hitchens-obraz.netlify.app/assets/images/divider.svg) (while the neighbouring *`icon-512.png`* [does](https://hitchens-obraz.netlify.app/assets/images/icon-512.png)).
