import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import norm
import numpy as np
import matplotlib.patches as mpatches
from colour import Color
from statistical_hypothesis_testing.tails import Tail


def create_critical_region_plot(alphas=[0.05, ], x_min=-3, y_max=0.5, tails=Tail.TWO_TAILED):
    alphas = sorted(alphas, reverse=True)
    x_max = x_min * (-1)

    red = Color("red")
    colors = list(red.range_to(Color("white"),len(alphas)+1))
    alphas_with_colors = [(alphas[i], colors[-i-2]) for i in range(0, len(alphas))] 

    x = np.linspace(x_min, x_max, 100)
    y = scipy.stats.norm.pdf(x,mean,std)
    plt.plot(x,y, color='black')

    def generate_area(x1, x2, color):
        pt1 = x1
        plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1)], color='black')

        pt2 = x2
        plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2)], color='black')

        ptx = np.linspace(pt1, pt2, 10)
        pty = scipy.stats.norm.pdf(ptx,mean,std)

        plt.fill_between(ptx, pty, color=color, alpha='1.0')


    legend_patches = []
    for alpha, color in alphas_with_colors:
        generate_area(x_min, norm.ppf(alpha/2), str(color))
        generate_area(norm.ppf(1 - alpha/2), x_max, str(color))
        legend_patches.append(mpatches.Patch(color=str(color), label=r'$\alpha = {:.2f} $'.format(alpha)))

    plt.legend(handles=legend_patches)

    plt.grid()

    plt.xlim(x_min,x_max)
    plt.ylim(0,y_max)

    plt.title('Critical Regions for z-test',fontsize=10)

    plt.xlabel('x')

    plt.savefig("normal_distribution_2.png")
    plt.show()

create_critical_region_plot([0.05,0.01,0.1])
