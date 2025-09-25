# C-inputs
## Gathering Parameters
### Grain Moisture Content
Following is the grain moisture content for each plant, along with reference.

Maize: 13% - Martin, 1949
Rice: 13% - Makky, 2019
Yam: 70% - Amankwah, 2019
Sorghum: 12% - [Purdue University](https://www.extension.purdue.edu/extmedia/AE/AE-82-w.html#:~:text=HARVEST%20CONDITIONS,are%20helpful%20if%20heads%20droop)
Millet: 12% - Ramashia, 2017
Groundnut: 10% - Ahmad, 2012
Cowpea: 10% - AWOSANMI, 2019
Soyabean: 13% - SDSU Extension, 2019
### Harvest Index
It is calculated as the ratio of the yield of the harvestable product to the total aboveground biomass. This can be used to plug into the Bolinder equation. Where possible, the minimum value was used. 

Maize: 0.48 - Maas & Lal, 2022
Rice: 0.17 - [source](https://academic.oup.com/jxb/article/61/12/3177/425540)
Yam: 0.50 - Yam's unavailable, but sweet potato roughly [was](https://journalissues.org/wp-content/uploads/sites/5/2018/07/Nwankwo-et-al-1.pdf)
Sorghum: 0.29 (conservative estimate) - Mishra, 1992
Millet: 34% - Mohammadi, 2018
Groundnut: 37% - Swetha, 2019
Cowpea: 23% (lowest, conservative value) - Dangi, 2020
Soyabean: 0.34 - Maas & Lal, 2022
### Root to Shoot ratio
Using the lowest, most conservative estimate possible ([Perplexity search](https://www.perplexity.ai/search/what-s-the-harvest-yield-of-gr-a3ZRCNlsTwGW3FB9s57HBw#3)).

Maize: 0.1
Rice: 0.2
Yam - is a root, so it doesn't matter - we can exclude $C_R$, as that's represented by the $C_P$, or harvested biomass (as the root is the harvested product).
Sorghum: 0.01
Millet: 0.2
Groundnut: 0.1 (the yielded nut isn't the entire root, though it's underground)
Cowpea: 0.1
Soyabean: 0.09

### Root Exudates
Root exudates are estimated to represent 5–21% of all photosynthetically-fixed C in plants and trees ([Zhang, 2024](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1423703/full#B11)). Let's choose 5% as a minimum estimate.

This means that 5% of the plant carbon is represented by root exudates. This translates to:
$$\frac{C_E}{(C_P + C_S + C_R + C_E)} = 0.05$$
$$=>C_E = 0.05 \times(C_P + C_S + C_R + C_E)$$
Bringing $C_E$ on one side, and solving:
$$C_E - 0.05 \times C_E= 0.05 \times(C_P + C_S + C_R)$$
$$0.95 \times C_E = 0.05 \times(C_P + C_S + C_R)$$
$$ C_E = \frac{0.05}{0.95} \times(C_P + C_S + C_R)$$
$$ C_E = 0.0526 \times(C_P + C_S + C_R)$$
## Bolinder Equation
Now, we are ready to plug these parameters into the Bolinder equation, which is basically used for calculating the $C_I$, or the carbon-inputs to the soil.

$$C_I = (C_P * S_P) + (C_S * S_S) + (C_R * S_R) + (C_E * S_E) $$

Next, **write a script** to plug my yield data values (subtracted by the standard error) - into the Bolinder equation, and output them nicely onto the results-screen.

# Open Pan Evaporation

Estimating OPE requires us to calculate the PET (Potential Evapo-Transpiration), which can be calculated using Malmstrom (1969) equation from Chapter 7 in Dingman's book (reference pg. 310). Alternatively, using a radiation-based approach from Tegos, 2017 (which requires some calibration, but is also very accurate). However, this was estimated using default factors for now.



