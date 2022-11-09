Changelog
=========

All notable changes to this project will be documented in this file.


Unreleased
==========

- add light_color and dark_color arguments to plottable.font autoset fontcolor functions
- inverse the yaxis of the table axes. This aligns the indices of table.rows with the integer location (iloc) of the row in the DataFrame.
Alongside that change col_label_row and col_group_labels now have negative indices (y-locations).
- add an apply_formatter function to formatters. This can now be used to also apply builtin string formatter syntax within plots (TODO).
- allow for custom height of col_label_row
- require python>=3.10
- add Bohndesliga table example

0.1.3
=====

- Allow for string representations of builtin string formatters to ColumnDefinitions formatters.


0.1.2
=====

Fixed
-----
- Fix bboxes not being drawn for table texts


Documentation
-------------
- Add .readthedocs.yaml config