# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:30:52 2017

@author: rmatam
"""

import seaborn as sns
sinplot()
sns.despine()
current_palette = sns.color_palette()
sns.palplot(current_palette)
sns.palplot(sns.color_palette("hls",8))
sns.palplot(sns.hls_palette(8,l=.3,s=.8))

plt.plot([0, 1], [0, 1], sns.xkcd_rgb["pale red"], lw=3)
plt.plot([0, 1], [0, 2], sns.xkcd_rgb["medium green"], lw=3)
plt.plot([0, 1], [0, 3], sns.xkcd_rgb["denim blue"], lw=3);

colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
sns.palplot(sns.xkcd_palette(colors))