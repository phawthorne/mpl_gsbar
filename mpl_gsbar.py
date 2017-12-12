import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def grouped_stacked_bar(ax, data, **kwargs):
    """

    Some needs for customizability: colors/alphas, labels, tickmarks

    :param ax:
    :param data: 3D np array indexed by group, bar, category
    :param kwargs:
    :return:
    """

    ngrps, nbars, ncats = data.shape

    # TODO: these need to be dynamic in response to # groups, bars, etc...
    # or customizable by user input.
    group_left_pos = [i+1.0 for i in range(ngrps)]
    bar_spacing = 0.15
    bar_width = 0.125
    tick_pos = [i+0.25 for i in group_left_pos]

    # set up the color array
    if 'cat_colors' in kwargs:
        cat_colors = kwargs['cat_colors']
    else:
        cat_colors = [None for c in range(ncats)]

    for b in range(nbars):
        bar_l = [g + b*bar_spacing for g in group_left_pos]
        bar_b = [0 for g in range(ngrps)]
        for c in range(ncats):
            bar_h = [data[g, b, c] for g in range(ngrps)]
            ax.bar(bar_l, bar_h, width=bar_width, bottom=bar_b, color=cat_colors[c])
            bar_b = [bar_b[g]+data[g, b, c] for g in range(ngrps)]


if __name__ == '__main__':
    test_data = np.random.random((2, 3, 4))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    grouped_stacked_bar(ax, test_data)
    plt.savefig('test.png', dpi=200)
    plt.close()

    cat_colors = ['orange', 'darkorchid', 'forestgreen', 'lightslategray']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    grouped_stacked_bar(ax, test_data, cat_colors=cat_colors)
    plt.savefig('test_cat_colors.png', dpi=200)
    plt.close()
