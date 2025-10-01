
# SOC sampling

FAO and IPCC best-practices were followed in soil sampling.

**Equation 2: Minimum Detectable Difference**

Details to be added, if necessary.

**Equation 3: Number of Samples**

Details to be added, if necessary.

# Processing in-situ SOC Data

## SOC mass by depth layer

**Equation 4:**

$$ M_{n,dl,SOC} = \frac{M_{n,dl,sample}}{\pi(\frac{D}{2})^2\times N} \times 10000  \times OC_{n,dl} $$

Where:
- $M_{n,dl,SOC}$ = SOC mass in soil sample n in depth layer dl (kg/ha)
- $M_{n,dl,sample}$ = Soil mass of sample n in depth layer dl (g)
- $D$  = Inside diameter of probe or auger
- $N$ = Number of cores sampled (unitless)
- $OC_{n,dl}$ = Organic carbon content in sample n in depth layer dl (g/kg)
- 10000 = g/mm $^2$ to kg/ha

This equation is only required when comparing measured SOC from year to year, and is hence not relevant at the validation stage. However, SOC and bulk density data was collected in two depth layers as approved under VM0042, and SOC content was thus calculated separately for each depth layer, to ensure comparison on an ESM (Equivalent Soil Mass) basis.
## Calculating SOC stocks

**Equation 5**

$$ SOC_{model} = 100 \times BD_{corr} \times OC_{n,dl} $$

Where:
- $SOC_{model}$ = SOC stock as model input data (t/ha)
- $BD_{corr}$ = Corrected bulk density of the fine soil fraction, after subtracting the mass proportion of the coarse fragments (g/cm $^3$ ) 
- $d$ = Soil depth (cm)
- 100 = Conversion factor from g/cm $^2$ to t/ha

In [RothC_Implementation_Axam/Axam_SOC_Data](https://github.com/mihirobendre/RothC_Implementation_Axam/tree/main/Axam_SOC_Data) the Python script `data_sorting.py` sorts the data from SOC sampling `SRI_LAB_VM0042_Project.xlsx`, separating the SOC data by depth layers (0-15cm and 15-30cm), and applying **Equation 5** to calculate SOC for each layer respectively, as well as the net SOC (combining both depth layers). The results of data processing are shown as:

```
SOC % (0-15 cm) average:  0.8508591549295774

BD (0-15 cm) average:  1.3674301116427434

SOC (0-15 cm) (g/cm^3):  1.1634904292176023

SOC (0-15 cm) (g/cm^2):  0.17452356438264036

SOC (0-15 cm) (t C/ha):  17.452356438264037

  

SOC % (15-30 cm) average:  0.6605106382978725

BD (15-30 cm) average:  1.4522895622895622

SOC (15-30 cm) (g/cm^3):  0.9592527057812166

SOC (15-30 cm) (g/cm^2):  0.14388790586718248

SOC (15-30 cm) (t C/ha):  14.388790586718248

  

Net SOC (0-30 cm) (t C/ha):  31.841147024982284
```

The value for Net SOC from processing the SOC data was used as the starting SOC stocks in the RothC SOC model script `RothC_Py.py` in both baseline and project scenarios.
# SOC Modeling

## Model inputs

After determining the initial SOC stocks from in-situ SOC sampling, lab analysis and processing, the remaining model inputs were determined, for running RothC for a 10-year future-projection. Following are the input parameters needed for a RothC model run:

### Soil parameters
#### Clay content
Clay content was analyzed in lab, when soil samples for SOC were collected.

#### IOM (Inert Organic Matter)
IOM was calculated from the equation provided in [RothC_description.pdf](https://github.com/mihirobendre/axam-docs/blob/main/References/RothC_description.pdf) , as shown:

$$ IOM = 0.049 \times SOC^{1.139} $$

Plugging in SOC = 31.841:

$$ IOM = 0.049 \times (31.841)^{1.139} = 2.524 $$

### Climate parameters

#### Precipitation (monthly average)
Average monthly precipitation for previous years can be calculated for the project area using the CHIRPS dataset, using a [Google Earth Engine script](https://code.earthengine.google.com/96e3ad1d956964cfd89fa646ec925c36), producing the [following graph](https://github.com/mihirobendre/axam-docs/blob/main/References/Axam_Rainfall_2024.png) for 2024. For estimating future rainfall, past year averages from [a Wikipedia article](https://github.com/mihirobendre/axam-docs/blob/main/References/Wa%2C%20Ghana%20-%20Wikipedia.pdf) were used.
#### Temperature (monthly average)
Average monthly temperature for previous years can be calculated for the project area using the TerraClimate dataset, using a [Google Earth Engine script](https://code.earthengine.google.com/198546b6d8902aee26c811bd7b46d3e6), producing the [following graph](https://github.com/mihirobendre/axam-docs/blob/main/References/Axam_Temp_2024.png) for 2024. For estimating future temperature, past year averages from [a Wikipedia article](https://github.com/mihirobendre/axam-docs/blob/main/References/Wa%2C%20Ghana%20-%20Wikipedia.pdf) were used.
#### Evaporation (monthly average)
As suggested by [RothC_description.pdf](https://github.com/mihirobendre/axam-docs/blob/main/References/RothC_description.pdf), monthly average evaporation has been estimated using the Potential Evapotranspiration, from the nearest site of Tamale, Ghana, from [Müller (1982)](https://github.com/mihirobendre/axam-docs/blob/main/References/Selected_climatic_data_global_set_standard_stations.pdf). Furthermore, Potential Evapotranspiration can be converted to Open Pan Evaporation by dividing by 0.75 (as instructed in [RothC_description.pdf](https://github.com/mihirobendre/axam-docs/blob/main/References/RothC_description.pdf)).

### Management inputs

#### Carbon inputs to soil

Carbon inputs to soil can be calculated as per the Bolinder equation, an approach suggested in [Maas and Lal (2022)](https://github.com/mihirobendre/axam-docs/blob/main/References/A%20case%20study%20of%20the%20RothC%20soil%20carbon%20model%20with%20potential%20evapotranspiration%20and%20remote%20sensing%20model%20inputs.pdf). Below is the Bolinder equation:

$$C_I = (C_P * S_P) + (C_S * S_S) + (C_R * S_R) + (C_E * S_E) $$

Where:
- $C_I$ is carbon-input to soil
- $C_P$ is carbon from harvested plant-matter
- $S_P$ is proportion of $C_P$ left on the field
- $C_S$ is carbon in stover (leftover plant-matter after harvest)
- $S_S$ is proportion of $C_S$ left on the field
- $C_R$ is carbon in roots
- $S_R$ is proportion of $C_R$ left on the field
- $C_E$ is carbon in root exudates
- $S_E$ is proportion of $C_E$ left on the field

To calculate $C_I$, we need to know the rest of the parameters in the Bolinder equation, which can be estimated using certain supporting parameters for each specific crop planted on the project area, namely Grain Moisture Content, Harvest Index, Root to Shoot Ratio and Root Exudates. 
##### Supporting Parameters
The following supporting parameters are required, for calculating the Carbon Inputs to the plant, and the sources are included [here](https://github.com/mihirobendre/axam-docs/tree/main/References/C_Input/Research_References).
###### Grain Moisture Content
Following is the grain moisture content for each plant, along with reference.
- Maize: 13% - Martin, 1949
- Rice: 13% - Makky, 2019
- Yam: 70% - Amankwah, 2019
- Sorghum: 12% - McKenzie, Purdue University
- Millet: 12% - Ramashia, 2017
- Groundnut: 10% - Ahmad, 2012
- Cowpea: 10% - Awosanmi, 2019
- Soyabean: 13% - SDSU Extension, 2019

###### Harvest Index
It is calculated as the ratio of the yield of the harvestable product to the total aboveground biomass. This can be used to plug into the Bolinder equation. Where possible, the minimum value was used. 

- Maize: 0.48 - Maas & Lal, 2022
- Rice: 0.17 - Yang, 2010
- Yam: 0.50 - Yam's unavailable, but sweet potato roughly - Nwankwo, 2018
- Sorghum: 0.29 (conservative estimate) - Mishra, 1992
- Millet: 34% - Mohammadi, 2018
- Groundnut: 37% - Swetha, 2019
- Cowpea: 23% (lowest, conservative value) - Dangi, 2020
- Soyabean: 0.34 - Maas & Lal, 2022

###### Root to Shoot Ratio
Using the lowest, most conservative estimate possible ([Perplexity search](https://www.perplexity.ai/search/what-s-the-harvest-yield-of-gr-a3ZRCNlsTwGW3FB9s57HBw#3)).

- Maize: 0.1
- Rice: 0.2
- Yam - is a root, so it doesn't matter - we can exclude $C_R$, as that's represented by the $C_P$, or harvested biomass (as the root is the harvested product).
- Sorghum: 0.01
- Millet: 0.2
- Groundnut: 0.1 (the yielded nut isn't the entire root, though it's underground)
- Cowpea: 0.1
- Soyabean: 0.09

###### Root Exudates
Root exudates are estimated to represent 5–21% of all photosynthetically-fixed C in plants and trees (Zhang, 2024). Let's choose 5% as a minimum estimate.

This means that 5% of the plant carbon is represented by root exudates. This translates to:
$$\frac{C_E}{(C_P + C_S + C_R + C_E)} = 0.05$$
$$=>C_E = 0.05 \times(C_P + C_S + C_R + C_E)$$

Bringing $C_E$ on one side, and solving:
$$C_E - 0.05 \times C_E= 0.05 \times(C_P + C_S + C_R)$$
$$0.95 \times C_E = 0.05 \times(C_P + C_S + C_R)$$
$$ C_E = \frac{0.05}{0.95} \times(C_P + C_S + C_R)$$
$$ C_E = 0.0526 \times(C_P + C_S + C_R)$$

##### Analysis 
Then, a dataset on Ghana's crop yields for the Upper West district, for each crop farmed in the region were estimated using the dataset [`Ghana_Crop_Data.csv`](https://github.com/mihirobendre/axam-docs/blob/main/References/C_Input/Ghana_Crop_Data.csv) from [Ghana Open Data Initiative](https://data.gov.gh/dataset/agricultural-production-estimates-1993-2017). Then, the Python script [`Yield_Estimation.py`](https://github.com/mihirobendre/axam-docs/blob/main/References/C_Input/Yield_Estimation.py) estimates the annual yield for each crop, within the Upper West region, and [`Analysis.py`](https://github.com/mihirobendre/axam-docs/blob/main/References/C_Input/Analysis.py) uses all the supporting parameters found above, and utilizes them for the Bolinder equation. The results are stored into `output.csv`. Finally, in [Final_C_input_Calculation.xlsx](https://github.com/mihirobendre/axam-docs/blob/main/References/C_Input/Final_C_input_Calculation.xlsx) these results are used in conjunction with known estimates of coverage of each crop on the project area, in order to estimate the total Carbon Input in the project and baseline scenarios.
#### Farm Yard Manure
Farm Yard Manure application is estimated from known estimates of dung application in the baseline scenario, and projected changes in dung application under the project scenario, as outlined in [`FYM_Estimation.xlsx`](https://github.com/mihirobendre/axam-docs/blob/main/References/Farm_Yard_Manure/FYM_Estimation.xlsx). 
#### DPM/RPM ratio
The default value of 1.44, as recommended for croplands in [RothC_description.pdf](https://github.com/mihirobendre/axam-docs/blob/main/References/RothC_description.pdf) is used.

## Model Calibration

The next step was to calibrate the RothC model, for which pedotransfer functions established in [Weihermüller, 2013](https://github.com/mihirobendre/axam-docs/blob/main/References/Calibration_Equations/Weihermller-etal-2013a.pdf), were used to calculate carbon pools in both project and baseline scenarios. The pedotransfer functions used are as follows:

$$ RPM = (0.1847 \times SOC + 0.1555) \times (clay+1.2750)^{-0.1158} $$

$$ HUM = (0.7148 \times SOC + 0.5069) \times (clay+0.3421)^{0.0184} $$

$$ BIO = (0.0140 \times SOC+0.0075) \times (clay+8.8473)^{0.0567} $$

Furthermore, based on the IOM equation, and DPM/RPM ratio, [RothC_description.pdf](https://github.com/mihirobendre/axam-docs/blob/main/References/RothC_description.pdf), we also know that:

$$ IOM = 0.049 \times SOC^{1.139} $$

$$ DPM = 1.44 \times RPM $$

## Model Run

After applying calibration equations, the RothC model was run (satisfying Equation 6) in both project and baseline scenarios, as found on [RothC_Implementation_Axam](https://github.com/mihirobendre/RothC_Implementation_Axam/tree/main) which gave both monthly and yearly results. The yearly results for both baseline and project scenarios were compiled in [Axam_Results.xlsx](https://github.com/mihirobendre/RothC_Implementation_Axam/blob/main/Axam_Results.xlsx), along with an error estimation through analytical error propagation method permitted in VM0042.

**Equation 6**:

$$ SOC_{bsl,i,t} = \int(SOC_{bsl,i,t}) $$

Where:
- $SOC_{bsl,i,t}$ = Estimated carbon stocks in the SOC pool in the baseline scenario for quantification unit i at the end of year t (tCO2e/ha)
- $\int(SOC_{bsl,i,t})$ = Modeled SOC stocks in the baseline scenario for quantification unit i in year t, calculated by modeling SOC stock changes over the course of the preceding year (tCO2e/ha)
- i = Quantification unit

# Error Analysis

VM0042 allows for error analysis via two methods:
1. Analytical error propagation, or
2. Monte Carlo simulation

Within analytical error propagation, VM0042 describes three individual sources of error, for which Equations 60-64 are utilized:
1. Model Prediction Error (structural error in the model)
2. Model Input and Measurement Error (considered insignificant, thus excluded)
3. Sampling Error (from soil sampling)

## Model Prediction Error 
This source of error is compiled in [Axam_Results.xlsx](https://github.com/mihirobendre/RothC_Implementation_Axam/blob/main/Axam_Results.xlsx). For projects in their initial stages, VM0042 allows for the estimation of Model Prediction Error by citing data from literature, instead of setting up baseline and project area plots - which is necessary in the monitoring stages. 
## Sampling Error
Sampling error comes from the variance in soil sampling, which depends on the number of samples, and the variety of soil types which were sampled. Sampling error was calculated using the [`sampling_error_estimation.py`](https://github.com/mihirobendre/RothC_Implementation_Axam/blob/main/Axam_SOC_Data/sampling_error_estimation.py) Python script, and then compiled in [Axam_Results.xlsx](https://github.com/mihirobendre/RothC_Implementation_Axam/blob/main/Axam_Results.xlsx).
## Combined Error
Lastly, model error and sampling error are combined using **Equation 63**, and the deducted from the estimated ERs from the SOC pool's difference between project and baseline scenarios.




















