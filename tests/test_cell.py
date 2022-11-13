import matplotlib

from plottable import __version__
from plottable.cell import Column, Row, SubplotCell, TextCell, create_cell
from plottable.column_def import ColumnType
from plottable.plots import percentile_bars


def test_version():
    assert __version__ == "0.1.5"


class TestDefaultCell:
    def test_default_cell_xy(self, default_cell):
        assert default_cell.xy == (0, 0)

    def test_default_cell_width(self, default_cell):
        assert default_cell.width == 1

    def test_default_cell_height(self, default_cell):
        assert default_cell.height == 1

    def test_default_cell_x(self, default_cell):
        assert default_cell.x == 0

    def test_default_cell_y(self, default_cell):
        assert default_cell.y == 0


class TestCustomCell:
    def test_custom_cell_xy(self, custom_cell):
        assert custom_cell.xy == (1, 2)

    def test_custom_cell_width(self, custom_cell):
        assert custom_cell.width == 3

    def test_custom_cell_height(self, custom_cell):
        assert custom_cell.height == 4

    def test_custom_cell_x(self, custom_cell):
        assert custom_cell.x == 1

    def test_custom_cell_y(self, custom_cell):
        assert custom_cell.y == 2


class TestTableCell:
    def test_table_cell_xy(self, table_cell):
        assert table_cell.xy == (1, 2)

    def test_table_cell_content(self, table_cell):
        assert table_cell.content == "String Content"

    def test_table_cell_row_idx(self, table_cell):
        assert table_cell.row_idx == 1

    def test_table_cell_col_idx(self, table_cell):
        assert table_cell.col_idx == 2

    def test_table_cell_width(self, table_cell):
        assert table_cell.width == 3

    def test_table_cell_height(self, table_cell):
        assert table_cell.height == 4

    def test_table_cell_rect_kw(self, table_cell):
        assert table_cell.rect_kw == {
            "linewidth": 0.0,
            "edgecolor": table_cell.ax.get_facecolor(),
            "facecolor": table_cell.ax.get_facecolor(),
            "width": 3,
            "height": 4,
        }

    def test_rectangle_patch(self, table_cell):
        _rect = matplotlib.patches.Rectangle(table_cell.xy, **table_cell.rect_kw)
        assert table_cell.rectangle_patch.xy == _rect.xy
        assert table_cell.rectangle_patch.get_width() == _rect.get_width()
        assert table_cell.rectangle_patch.get_height() == _rect.get_height()


class TestTextCell:
    def test_table_cell_textprops(self, text_cell):
        assert text_cell.textprops == {"ha": "right", "va": "center"}

    def test_table_padding(self, text_cell):
        assert text_cell.padding == 0.1

    def test_table_default_ha(self, text_cell):
        assert text_cell.ha == "right"

    def test_set_text(self, text_cell):
        _text = matplotlib.text.Text(
            text_cell.x + text_cell.width - text_cell.padding * text_cell.width,
            text_cell.y + text_cell.height / 2,
            "String Content",
        )

        text_cell.draw()
        assert text_cell.text.get_text() == _text.get_text()
        assert text_cell.text.get_position() == _text.get_position()

    def test_set_text_ha_is_left(self, text_cell):
        text_cell.ha = "left"
        text_cell.draw()

        x, _ = text_cell.text.get_position()
        assert x == text_cell.x + text_cell.padding * text_cell.width

    def test_set_text_ha_is_center(self, text_cell):
        text_cell.ha = "center"
        text_cell.draw()

        x, _ = text_cell.text.get_position()
        assert x == text_cell.x + text_cell.width / 2


class TestSubplotCell:
    def test_subplot_cell_plot_fn(self, subplot_cell):
        assert subplot_cell._plot_fn == percentile_bars

    def test_subplot_cell_plot_kw(self, subplot_cell):
        assert subplot_cell._plot_kw == {}

    def test_subplot_cell_make_axes_inset(self, subplot_cell):
        subplot_cell.make_axes_inset()
        assert isinstance(subplot_cell.axes_inset, matplotlib.axes.Axes)

    def test_get_rectangle_bounds(self, subplot_cell):
        # TODO
        assert True

    def test_subplot_cell_plot(self, subplot_cell):
        subplot_cell.make_axes_inset()
        subplot_cell.plot()
        assert len(subplot_cell.axes_inset.patches) > 1


def test_create_cell_type_is_stringcell():
    assert (
        type(
            create_cell(
                column_type=ColumnType.STRING,
                xy=(0, 0),
                content="A",
                row_idx=0,
                col_idx=0,
            )
        )
        == TextCell
    )


def test_create_cell_type_is_subplotcell():
    assert (
        type(
            create_cell(
                column_type=ColumnType.SUBPLOT,
                xy=(0, 0),
                content="A",
                row_idx=0,
                col_idx=0,
                plot_fn=percentile_bars,
            )
        )
        == SubplotCell
    )


def test_row_of_subplot_cells_does_not_raise_on_set_fontproperties():
    cells = [
        create_cell(
            column_type=ColumnType.SUBPLOT,
            xy=(0, i),
            content=i,
            row_idx=i,
            col_idx=0,
            plot_fn=percentile_bars,
        )
        for i in range(5)
    ]

    row = Column(cells, index=0)

    row.set_fontcolor("k")
    row.set_fontfamily("Arial")
    row.set_fontsize(10)
    row.set_ha("right")
    row.set_ma("right")


def test_row_height():
    cells = [
        create_cell(
            column_type=ColumnType.STRING,
            xy=(i, 0),
            content=i,
            row_idx=0,
            col_idx=i,
            height=2,
        )
        for i in range(5)
    ]
    row = Row(cells, index=0)
    assert row.height == 2


def test_row_x():
    cells = [
        create_cell(
            column_type=ColumnType.STRING,
            xy=(i + 2, 0),
            content=i,
            row_idx=0,
            col_idx=i,
        )
        for i in range(5)
    ]
    row = Row(cells, index=0)
    assert row.x == 2


def test_row_y():
    cells = [
        create_cell(
            column_type=ColumnType.STRING,
            xy=(i, 2),
            content=i,
            row_idx=0,
            col_idx=i,
        )
        for i in range(5)
    ]
    row = Row(cells, index=0)
    assert row.y == 2


def test_column_width():
    cells = [
        create_cell(
            column_type=ColumnType.STRING,
            xy=(0, i),
            content=i,
            row_idx=i,
            col_idx=0,
            width=2,
        )
        for i in range(5)
    ]
    col = Column(cells, index=0)
    assert col.width == 2


def test_column_x():
    cells = [
        create_cell(
            column_type=ColumnType.STRING,
            xy=(2, i),
            content=i,
            row_idx=i,
            col_idx=0,
        )
        for i in range(5)
    ]
    col = Column(cells, index=0)
    assert col.x == 2


def test_column_y():
    cells = [
        create_cell(
            column_type=ColumnType.STRING,
            xy=(0, i + 2),
            content=i,
            row_idx=i,
            col_idx=0,
        )
        for i in range(5)
    ]
    col = Column(cells, index=0)
    assert col.y == 2
