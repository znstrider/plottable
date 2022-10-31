
Contributor Guide
=================

*Contributors are very welcome to this project.*  

You can contribute by giving feedback:

At this stage, **usability** and **clarity** are a main priority.
- If there is something that you think doesn't make sense, is too hard to do, worded badly or should work differently etc., don't hesitate to open an issue or get in touch.

- If there is something you would like mpltable to do, but it currently lacks the functionality, open an issue.

- If you'd like to review the code and have suggestions on how to structure the project better, I'm all ears!

**You are also very welcome to contribute to the package by creating a Pull Request.**

If you are relatively new to contributing to projects or need a refresher on the process, you can read this great `Step-by-step guide to contribute on GitHub <https://www.dataschool.io/how-to-contribute-on-github/>`_ 

If you want to contribute to the project, best use an editable installation:

.. code-block::

    git clone https://github.com/znstrider/mpltable.git
    cd mpltable

    pip install -e .

Any contribution to documentation and examples is also very welcome.


Code Formatting
---------------

This project uses the black code formatter to ensure all code conforms to a specified format. It is necessary to format the code using black prior to committing. You can do this by manually running the `black` command to run black on all .py files, or with `black <filename.py>` to run it on a specific file.

Alternatively, you can setup black autoformatting within your IDE.