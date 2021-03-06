import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import norm
import numpy as np
import matplotlib.patches as mpatches
from colour import Color
from ..tails import Tail


def create_critical_region_plot(alphas=[0.05, ], tails=Tail.TWO_TAILED, x_min=-3, y_max=0.5):
    alphas = sorted(alphas, reverse=True)
    x_max = x_min * (-1)

    red = Color("#FF7F50")
    colors = list(red.range_to(Color("white"),len(alphas)+1))
    alphas_with_colors = [(alphas[i], colors[-i-2]) for i in range(0, len(alphas))] 

    x = np.linspace(x_min, x_max, 100)
    y = scipy.stats.norm.pdf(x)
    plt.plot(x,y, color='black')

    def generate_area(x1, x2, color):
        pt1 = x1
        plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1)], color='black')

        pt2 = x2
        plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2)], color='black')

        ptx = np.linspace(pt1, pt2, 10)
        pty = scipy.stats.norm.pdf(ptx)

        plt.fill_between(ptx, pty, color=color, alpha='1.0')


    legend_patches = []
    for alpha, color in alphas_with_colors:
        if tails == Tail.TWO_TAILED:
            generate_area(x_min, norm.ppf(alpha/2), str(color))
            generate_area(norm.ppf(1 - alpha/2), x_max, str(color))
        elif tails == Tail.LEFT_TAILED:
            generate_area(x_min, norm.ppf(alpha), str(color))
        elif tails == Tail.RIGHT_TAILED:
            generate_area(norm.ppf(1 - alpha), x_max, str(color))
        legend_patches.append(mpatches.Patch(color=str(color), label=r'$\alpha = {:.2f} $'.format(alpha)))

    plt.legend(handles=legend_patches)

    plt.grid()

    plt.xlim(x_min,x_max)
    plt.ylim(0,y_max)

    plt.title('Kritické obory pro z-test',fontsize=10)
    plt.xlabel('x')

    plt.savefig("z_test_critical_region.png")
    plt.show()

def create_p_value_plot(statistics,alpha=0.05, tails=Tail.TWO_TAILED, x_min=-3, y_max=0.5, lang='en'):
    x_max = x_min * (-1)

    x = np.linspace(x_min, x_max, 100)
    y = scipy.stats.norm.pdf(x)
    plt.plot(x,y, color='black')

    def generate_area(x1, x2, color,hatch=None,edgecolor=None):
        pt1 = x1
        plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1)], color='black')

        pt2 = x2
        plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2)], color='black')

        ptx = np.linspace(pt1, pt2, 100)
        pty = scipy.stats.norm.pdf(ptx)

        plt.fill_between(ptx, pty, facecolor=color, alpha='1.0', hatch=hatch, edgecolor=edgecolor)

    if tails == Tail.TWO_TAILED:
        generate_area(x_min, norm.ppf(alpha/2), '#FF7F50')
        generate_area(norm.ppf(1 - alpha/2), x_max, '#FF7F50')
        generate_area(x_min, -abs(statistics), 'none', hatch='//////', edgecolor='#5B84B1FF')
        generate_area(abs(statistics), x_max, 'none', hatch='//////', edgecolor='#5B84B1FF')
    elif tails == Tail.LEFT_TAILED:
        generate_area(x_min, norm.ppf(alpha), '#FF7F50')
        generate_area(x_min, statistics, 'none', hatch='//////', edgecolor='#5B84B1FF')
    elif tails == Tail.RIGHT_TAILED:
        generate_area(norm.ppf(1 - alpha), x_max, '#FF7F50')
        generate_area(statistics, x_max, 'none', hatch='//////', edgecolor='#5B84B1FF')

    

    plt.grid()

    plt.xlim(x_min,x_max)
    plt.ylim(0,y_max)

    legend_patches = []
    if lang == 'en':
        plt.title('p-value of z-test',fontsize=10)
        legend_patches.append(mpatches.Patch(color='#FF7F50', label='Critical Region'.format(alpha)))
        legend_patches.append(mpatches.Patch(color='#5B84B1FF', label='p-value'.format(alpha)))
    elif lang == 'cs':
        plt.title('p-hodnota z-testu',fontsize=10)
        legend_patches.append(mpatches.Patch(color='#FF7F50', label='Kritický obor'.format(alpha)))
        legend_patches.append(mpatches.Patch(facecolor='none', hatch='//////', edgecolor='#5B84B1FF', label='p-hodnota'.format(alpha)))
    plt.legend(handles=legend_patches)
    plt.xlabel('x')

    plt.savefig("z_test_p_value.png")
    plt.show()
