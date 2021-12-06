
# LIBRARIES ----

import pandas as pd
import pandas_profiling as pf

from plotnine import (
    ggplot, aes, geom_point, geom_smooth, labs,
    theme_xkcd
)


# DATASET ----

mpg_df = pd.read_csv("mpg.csv")


# PANDAS PROFILING ----

rpt = pf.ProfileReport(mpg_df)

rpt.to_file('pandas_profiling/profile_report.html')


# PLOTNINE BONUS ----

ggplot(
    aes('horsepower', 'mpg'),
    data = mpg_df
) \
    + geom_point() \
    + geom_smooth(
        method = 'loess', 
        span   = 0.8,
        color  = "dodgerblue"
    ) \
    + labs(
        title = "Trend of Horsepower vs Fuel Economy"
    ) \
    + theme_xkcd()
