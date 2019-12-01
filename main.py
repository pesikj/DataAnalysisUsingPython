from statistical_hypothesis_testing.plots import plots_z_test
from statistical_hypothesis_testing.tails import Tail


#plots_z_test.create_critical_region_plot(alphas=[0.1, 0.05, 0.01], tails=Tail.RIGHT_TAILED)
plots_z_test.create_p_value_plot(0.5109,alpha=0.05,lang='cs', tails=Tail.RIGHT_TAILED)
