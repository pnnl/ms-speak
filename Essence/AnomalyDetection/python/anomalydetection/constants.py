
# 1=on 0=off
HISTOGRAMS_DEBUG = 1

# see svm_calc.py:cross_validate
NU_START_POW_HIGH = -1;
NU_START_POW_LOW = -5;
NU_BASE_LIST = [1, 3];
 # if we pick a nu that is the highest or lowest in the test range, we expand the range in that direction and check again
 # It runs out we can't expand in the _HIGH direction because libsvm requires nu to be < 1 (and also >= 0)
NU_EXPAND_INCREMENT = 3;
