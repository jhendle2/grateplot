# GratePlot
## v1.0, 7/23/2020

Python 3 library for designing matrices with functional determined elements (aka grates)

Designed by Jonah Hendler

# Initialization
Please make sure you have properly installed MatPlotLib v3.3.0 or a later version

# How To Use
## Step 1: Creating a Grate
Create a Grate object like so:
`test_grate = grate(num_rows, num_cols)`

For example, a grate of size 5x6 would be:
`grate_5x6 = grate(5, 6)`

## Step 2: Filling your Grate
Fill the grate with the following functions:

`.fill(fill_value)`

`.fill_random(low, high)` Note: low defaults to 0, high to 10

`.fill_rule(rule)` where `rule` is a function which takes in two variables, row (n) and column (m)

__Note:__ Rules may be placed in the `rules.py` file for convenience,
and should only contain the parameters `n` and `m` if they
are to be used in `.fill_rule()`

## Step 3: Outputting your Grate
### Printing
To print your grate, type the following:
`print(test_grate)`

If you would like axes in your printing, use:
`print(test_grate.__repr__(axes=True))`

You can also force the print to use a specific set of characters:
`print(test_grate.__repr__(force_chars=['A', 'B', 'C']))`

### Plotting
To plot your grate, you can use the following methods:

`test_grate.plot_color(color, show_digits)`

`color` can be assigned with `plt.cm.` followed by a pluralized color name
`show_digits` will either show digits on the plot (True) or not (False)

You may also save the grate plot with:

`test_grate.save(color, show_digits, file_name, res)`

Which behaves similarly to `.plot()`

`file_name` is the file name + file type you wish to
use and `res` is the resolution of the image in DPI

The function `.plot_and_save()` performs the functions
of both `.plot_color()` and `.save()`

---

I hope you enjoy my library!

-Jonah