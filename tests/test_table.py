import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest

from plottable import ColDef, ColumnDefinition, Table, formatters, plots
from plottable.cell import SubplotCell


def test_table_df(df):
    tab = Table(df)
    assert tab.df.equals(df)


def test_table_df_index_name(table):
    assert table.df.index.name == "index"


def test_index_col(df):
    tab = Table(df, index_col="A")
    assert tab.index_col == "A"
    assert tab.df.shape[1] == 4


def test_columns(df):
    tab = Table(df, columns=["A", "B"])
    assert tab.df.columns.to_list() == ["A", "B"]


def test_cell_kw(df):
    tab = Table(df, cell_kw={"linewidth": 2})
    assert "linewidth" in tab.cell_kw
    assert tab.cell_kw["linewidth"] == 2

    for cell in tab.cells.values():
        assert cell.rectangle_patch.get_linewidth() == 2


def test_col_label_row(table, df):
    for col_idx, cell in enumerate(table.col_label_row.cells):
        assert cell.y == cell.row_idx
        assert cell.col_idx == col_idx


def test_table_axes(table):
    assert table.ax == plt.gca()


def test_table_figure(table):
    assert table.figure == plt.gca().figure


def test_table_df_n_rows(table, df):
    assert table.n_rows == len(df)


def test_table_df_n_cols(table, df):
    assert table.n_cols == len(df.columns)


def test_table_column_names(table, df):
    assert table.column_names == ["index"] + list(df.columns)


def test_table_column_definitions(table):
    for col in table.column_names:
        assert (
            table.column_definitions[col]
            == ColumnDefinition(name=col)._as_non_none_dict()
        )


def test_get_column_titles(table):
    assert table._get_column_titles()[0] == table.df.index.name
    assert table._get_column_titles()[1:] == ["A", "B", "C", "D", "E"]


def test_get_col_groups_are_empty(table):
    assert table._get_col_groups() == set()


def test_get_col_groups(df):
    tab = Table(
        df,
        column_definitions=[
            ColumnDefinition(name, group="group1") for name in ["A", "B"]
        ],
    )
    assert tab._get_col_groups() == set(["group1"])


def test_get_col_groups_multiple_groups(df):
    tab = Table(
        df,
        column_definitions=[ColumnDefinition(name, group=name) for name in df.columns],
    )
    assert tab._get_col_groups() == set(df.columns)


def test_get_non_group_colnames(df):
    tab = Table(
        df,
        column_definitions=[
            ColumnDefinition(name, group="group1") for name in ["A", "B"]
        ],
    )
    assert tab._get_non_group_colnames() == set(["index", "C", "D", "E"])


def test_get_non_group_colnames_is_empty_set(df):
    tab = Table(
        df,
        column_definitions=[
            ColumnDefinition(name, group=name) for name in list(df.columns) + ["index"]
        ],
    )
    assert tab._get_non_group_colnames() == set()


def test_table_column_name_to_idx(table):
    assert table.column_name_to_idx == {
        "index": 0,
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
    }


def test_table_cell_kw_is_empty_dict(table):
    assert table.cell_kw == {}


def test_table_cell_kw(df):
    tab = Table(df, cell_kw={"linewidth": 2})
    assert tab.cell_kw == {"linewidth": 2}


def test_get_column_textprops_default(table):
    col_def_dict = ColumnDefinition("A")._as_non_none_dict()
    textprops = table._get_column_textprops(col_def_dict)
    assert textprops == {"ha": "right", "multialignment": "right"}


def test_get_column_textprops_added_kw(table):
    col_def_dict = ColumnDefinition(
        "A", textprops={"size": 16, "weight": "bold"}
    )._as_non_none_dict()
    textprops = table._get_column_textprops(col_def_dict)
    assert textprops == {
        "ha": "right",
        "multialignment": "right",
        "size": 16,
        "weight": "bold",
    }


def test_get_column_textprops_replace_default_kw(table):
    col_def_dict = ColumnDefinition("A", textprops={"ha": "center"})._as_non_none_dict()
    textprops = table._get_column_textprops(col_def_dict)
    assert textprops == {"ha": "center", "multialignment": "center"}


def test_textprops_is_default(table):
    assert table.textprops == {"ha": "right"}


def test_textprops(df):
    tab = Table(df, textprops={"fontsize": 14})
    assert tab.textprops == {"ha": "right", "fontsize": 14}


def test_celltext_textprops(table):
    for cell in table.cells.values():
        assert cell.textprops == {
            "ha": "right",
            "va": "center",
            "multialignment": "right",
        }


def test_celltext_bbox_textprop(df):
    boxprops = {"boxstyle": "circle"}
    tab = Table(df, textprops={"bbox": boxprops})
    for cell in tab.cells.values():
        assert cell.textprops == {
            "ha": "right",
            "va": "center",
            "multialignment": "right",
            "bbox": boxprops,
        }


def test_init_table_columns(table):
    table._init_columns()
    assert list(table.columns.keys()) == table.column_names


@pytest.mark.parametrize(
    "colname,idx", [("index", 0), ("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]
)
def test_initialized_table_columns(table, colname, idx):
    table._init_columns()
    assert colname in table.columns.keys()
    col = table.columns[colname]
    assert col.index == idx
    assert col.cells == []
    assert col.name == colname


def test_init_table_rows(table):
    table._init_rows()
    assert list(table.rows.keys()) == list(range(len(table.df)))


def test_table_row_indices(df):
    tab = Table(df)

    first_row = tab.rows[0]
    df_row_values = df.to_records()[0]

    for cell, value in zip(first_row.cells, df_row_values):
        assert cell.content == value


def test_col_label_row_index(table):
    assert table.col_label_row.index == -1


def test_group_label_row_index(table):
    assert table.col_label_row.index == -1


def test_get_column(table):
    col = table.get_column("A")
    assert col.index == 1
    assert col.name == "A"
    assert len(col.cells) == len(table.df)


def test_get_column_by_index(table):
    col = table.get_column_by_index(1)
    assert col.index == 1
    assert col.name == "A"
    assert len(col.cells) == len(table.df)


def test_get_row(table):
    row_data = table.df.to_records()
    row = table._get_row(0, row_data[0])
    assert len(row_data[0]) == len(row.cells)


def test_xlim(table):
    assert table.ax.get_xlim() == (-0.025, table.df.shape[1] + 1 + 0.025)


def test_ylim(table):
    assert table.ax.get_ylim() == (len(table.df) + 0.05, -1.025)


def test_get_column_widths(table):
    assert table._get_column_widths() == [1] * (table.df.shape[1] + 1)


def test_get_custom_column_widths(df):
    tab = Table(df, column_definitions=[ColumnDefinition("E", width=2)])
    assert tab._get_column_widths() == [1] * (tab.df.shape[1]) + [2]


def test_get_custom_index_column_widths(df):
    tab = Table(df, column_definitions=[ColumnDefinition("index", width=2)])
    assert tab._get_column_widths() == [2] + [1] * (tab.df.shape[1])


def test_get_even_rows(table):
    assert table.get_even_rows() == list(table.rows.values())[::2]


def test_get_odd_rows(table):
    assert table.get_odd_rows() == list(table.rows.values())[1::2]


def test_set_alternating_row_colors_even_rows(table):
    color = (0.9, 0.9, 0.9, 1)
    table.set_alternating_row_colors(color)
    for row in table.get_even_rows():
        for cell in row.cells:
            assert cell.rectangle_patch.get_facecolor() == color


def test_set_alternating_row_colors_odd_rows(table):
    color2 = (0.9, 0.9, 0.9, 1)
    table.set_alternating_row_colors(color2=color2)
    for row in table.get_odd_rows():
        for cell in row.cells:
            assert cell.rectangle_patch.get_facecolor() == color2


def test_set_alternating_row_colors_odd_and_even_rows(table):
    color = (0.9, 0.9, 0.9, 1)
    color2 = (0.85, 0.85, 0.85, 1)
    table.set_alternating_row_colors(color=color, color2=color2)

    for row in table.get_even_rows():
        for cell in row.cells:
            assert cell.rectangle_patch.get_facecolor() == color

    for row in table.get_odd_rows():
        for cell in row.cells:
            assert cell.rectangle_patch.get_facecolor() == color2


def test_get_col_label_row(table):
    idx = len(table.df) + 1

    row = table._get_col_label_row(idx, table._get_column_titles())

    for col_idx, (cell, content) in enumerate(
        zip(row.cells, ["index", "A", "B", "C", "D", "E"])
    ):
        assert cell.content == content
        assert cell.row_idx == idx
        assert cell.col_idx == col_idx
        assert cell.xy == (col_idx, idx)


def test_get_subplot_cells_is_empty_dict(table):
    assert table._get_subplot_cells() == {}


def test_get_subplot_cells(df):
    def plot_fn(ax, arg):
        return None

    tab = Table(df, column_definitions=[ColumnDefinition("A", plot_fn=plot_fn)])

    subplot_cells = tab._get_subplot_cells()
    assert list(subplot_cells.keys()) == [(idx, 1) for idx in range(len(tab.df))]

    for cell in subplot_cells.values():
        assert hasattr(cell, "make_axes_inset")
        assert isinstance(cell, SubplotCell)


def test_table_make_subplots(df):
    def plot_fn(ax, arg):
        ax.plot([0, 0], [1, 1])

    tab = Table(df, column_definitions=[ColumnDefinition("A", plot_fn=plot_fn)])

    subplot_cells = tab._get_subplot_cells()

    for cell in subplot_cells.values():
        assert len(cell.axes_inset.get_lines()) > 0


def test_cell_text_is_formatted_by_formatter(df):

    col_defs = [ColDef("A", formatter=formatters.decimal_to_percent)]
    tab = Table(df, column_definitions=col_defs)

    for cell in tab.columns["A"].cells:
        cell_text = cell.text.get_text()
        assert len(cell_text) <= 4
        assert any([s in cell_text for s in ["–", "✓", "%"]])


def test_cell_text_is_formatted_by_string_formatter(df):
    tab = Table(df, column_definitions=[ColDef("A", formatter="{:.2f}")])
    for cell in tab.columns["A"].cells:
        cell_text = cell.text.get_text()
        assert len(cell_text) == 4


def test_table_apply_cmaps(df):
    tab = Table(df, column_definitions=[ColDef("B", cmap=mpl.colormaps["RdBu"])])
    base_cell_color = tab.cells[1, 1].rectangle_patch.get_facecolor()

    for cell in tab.columns["B"].cells:
        cell_color = cell.rectangle_patch.get_facecolor()
        assert cell_color != base_cell_color


def test_table_apply_text_cmaps(df):
    tab = Table(df, column_definitions=[ColDef("B", text_cmap=mpl.colormaps["RdBu"])])
    base_text_color = tab.cells[1, 1].text.get_color()

    for cell in tab.columns["B"].cells:
        cell_color = cell.text.get_color()
        assert cell_color != base_text_color


def test_col_label_row_height_is_set(df):
    tab = Table(df, col_label_cell_kw={"height": 2})

    for cell in tab.col_label_row.cells:
        assert cell.height == 2
        assert cell.rectangle_patch.get_height() == 2


def test_set_col_label_row_influences_col_group_label_y(df):
    tab = Table(df, col_label_cell_kw={"height": 2})

    for cell in tab.col_group_cells.values():
        assert cell.y == -2


# TODO
def test_table_plot_colgroup_headers(df):
    tab = Table(df)
    assert True


def test_table_plot_title_divider(df):
    tab = Table(df)
    assert True


def test_table_plot_row_dividers(df):
    tab = Table(df)
    assert True


def test_table_plot_column_borders(df):
    tab = Table(df)
    assert True


def test_plot_col_group_labels(table):
    pass


def test_plot_col_label_divider(table):
    pass


def test_plot_footer_divider(table):
    pass


def test_plot_row_dividers(table):
    pass


def test_plot_column_borders(table):
    pass


def test_plot_fn_with_formatter_does_not_raise(df):
    column_definitions = [
        ColDef(
            "A", plot_fn=plots.progress_donut, formatter=formatters.decimal_to_percent
        )
    ]

    tab = Table(df, column_definitions=column_definitions)
