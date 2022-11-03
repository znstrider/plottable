## Beautiful tables in matplotlib.

plottable is a Python library for plotting beautifully customized, presentation ready tables in Matplotlib.

To learn about its functionality, have a look at the [documentation](https://plottable.readthedocs.io/en/latest/).

### Quickstart

#### Installation

```
pip install plottable
```

#### A Basic Example
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plottable import Table

d = pd.DataFrame(np.random.random((5, 5)), columns=["A", "B", "C", "D", "E"]).round(2)
fig, ax = plt.subplots(figsize=(6, 5))
tab = Table(d)

plt.show()
```

<img src="docs/example_notebooks/images/basic_table.png" width="300">

### Redoing the [Reactable 2019 Women's World Cup Predictions Visualization](https://glin.github.io/reactable/articles/womens-world-cup/womens-world-cup.html)

You can find the [notebook here](https://github.com/znstrider/plottable/blob/master/docs/example_notebooks/wwc_example.ipynb)

<img src="docs/example_notebooks/images/wwc_table.png">

### Styling A Table

#### There are three main ways to customize a table:

##### 1) [By supplying keywords to the Table](https://plottable.readthedocs.io/en/latest/notebooks/table.html)

##### 2) [Providing a ColumnDefinition for each column you want to style](https://plottable.readthedocs.io/en/latest/notebooks/column_definition.html)

##### 3) [Accessing a tables rows or columns](https://plottable.readthedocs.io/en/latest/notebooks/rows_and_columns.html)

### Contributing

##### *Contributors are very welcome to this project.*  

Please take a look at the [Contributor Guide](contributing.rst)


### Credits

plottable is built for the lack of good table packages in the python ecosystem.
It draws inspiration from R packages [gt](https://github.com/rstudio/gt) and [reactable](https://github.com/glin/reactable), from blog posts about creating tables in matplotlib [Tim Bayer: How to create custom tables](https://matplotlib.org/matplotblog/posts/how-to-create-custom-tables/) and [Son of a corner: Beautiful Tables in Matplotlib, a Tutorial](https://www.sonofacorner.com/beautiful-tables/) and from matplotlibs own table module.