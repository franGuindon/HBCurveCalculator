HBCurveCalculator
=================

HBCurveCalculator is a python library used to compute magnetization curves for a variety of ferromagnetic materials. The magnetization curve is a nonlinear relation between B, the magnetic field density applied to a ferromagnetic core, and H, the resulting magnetic field intensity which is partially dependent on the properties of the material. As a quick clarification, this library presently does not support hysteresis and calculations with changing magnetic fields. It is intended for simple static field calculations.

Motivation
----------

When studying magnetic circuits, it becomes crucial to have a simple way to calculate and manipulate values on the magnetization curve for different materials. As part of my Electronic Power Preprocessing class our teacher showed us [Luis León's simple and magnific web app](https://github.com/lleon95/lleon95.github.io). However, one of my assignements required a more detailed manipulation and modeling of the magnetization curve. This library has been the result of taking ideas from Luis León's implementation and other relevant ideas.

Installation
------------

Step 1: The main prerequisite is to have Python 3.* installed. Then make sure to have Numpy and Matplotlib installed as well:

```console
$ python3 -m pip install numpy matplotlib
```

Step 2: Download the code or clone the repository:

```console
$ git clone git@github.com:franGuindon/HBCurveCalculator.git
```

Step 3: Since I did not use a setup system, the library script must be either manually moved to the same directory as the main script using it, moved to any of the directories on the python path or add its current directory to the python path.

Step 4: You are done and now you are ready to use this library.

Usage
-----

First move to the local repository directory:

```
$ cd PATH/TO/HBCurveCalculator/
```

To test the source and make sure it hasn't broken, run:

```console
$ python3 -m unittest
```
To use the script I developed for my specific class assignment, run:

```console
$ python3 examen_1.py
```

To use in your own scripts, simply make sure to follow Step 3 of the installation guide, then import the library into your script with:

```console
# your_script.py:

import libHBCurveCalculator        # or
import libHBCurveCalculator as hb  # or
from libHBCurveCalculator import * #
```