# Grate Library
import random
import rules
import matplotlib.pyplot as plt


class grate:

    @staticmethod
    def zeroes(rows, cols):
        grate = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            grate.append(row)
        return grate

    @staticmethod
    def str_element(element, force_chars):
        if force_chars is None:
            return str(element)
        else:
            return str(force_chars[element % len(force_chars)])

    def __init__(self, rows, cols):
        self.grate = self.zeroes(rows, cols)
        self.rows = rows
        self.cols = cols

    def num_rows(self):
        return self.rows

    def num_cols(self):
        return self.cols

    def set(self, row, col, item):
        self.grate[row][col] = item

    def fill(self, item):
        for r in range(self.rows):
            for c in range(self.cols):
                self.set(r, c, item)

    def fill_random(self, low=0, high=10):
        for r in range(self.rows):
            for c in range(self.cols):
                rand_int = random.randint(low, high)
                self.set(r, c, rand_int)

    def fill_rule(self, rule):
        for r in range(self.rows):
            for c in range(self.cols):
                self.set(r, c, rule(r, c))

    def str_axes(self, force_chars=None):
        out = ""
        for r in range(self.rows):
            if r == 0:
                out += "\t"
                for c in range(self.cols):
                    out += str(c) + "\t"
            else:
                out += "%s\t" % r
                for c in range(self.cols):
                    out += self.str_element(self.grate[r][c], force_chars)
                    out += "\t"
            out += "\n"
        return out

    def str_default(self, force_chars=None):
        out = ""
        for r in self.grate:
            for c in r:
                out += self.str_element(c, force_chars) + "\t"
            out += "\n"
        return out

    def plot(self, color=plt.cm.Blues, show_digits=False):
        fig, ax = plt.subplots()
        ax.matshow(self.grate, cmap=color)
        for i in range(self.rows):
            for j in range(self.cols):
                c = self.grate[i][j]
                if show_digits:
                    ax.text(j, i, str(c), va="center", ha="center")

    def plot_color(self, color=plt.cm.Blues, show_digits=False):
        self.plot(color,show_digits)
        plt.show()
        print("! Finished Plotting")

    def save(self, color=plt.cm.Blues, show_digits=False, file_name="plot.png", res=300):
        self.plot(color, show_digits)
        plt.savefig(file_name,dpi=res)
        print("! Finished Saving")

    def plot_and_save(self, color=plt.cm.Blues, show_digits=False, file_name="plot.png", res=300):
        self.save(color, show_digits, file_name, res)
        plt.show()
        print("! Finished Plotting")

    def __repr__(self, axes=False, force_chars=None):
        if axes:
            return self.str_axes(force_chars)
        else:
            return self.str_default(force_chars)


def test():
    g = grate(500, 500)
    g.fill_rule(rules.n3_contains_m)
    # print(g.__repr__(axes=True, force_chars=['A', 'B', 'C']))
    # print(g.__repr__(axes=False, force_chars=None))
    g.plot_and_save(color=plt.cm.Greys, file_name="grate.png", res=900)


# test()
