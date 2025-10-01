
# SOC sampling

FAO and IPCC best-practices were followed in soil sampling.

**Equation 2: Minimum Detectable Difference**

Details to be added.

**Equation 3: Number of Samples**

Details to be added.

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
Average monthly precipitation for previous years can be calculated for the project area using the CHIRPS dataset, using a [Google Earth Engine script](https://code.earthengine.google.com/96e3ad1d956964cfd89fa646ec925c36), producing the [following graph](https://github.com/mihirobendre/axam-docs/blob/main/References/Axam_Rainfall_2024.png). For estimating future rainfall, past averages were used from the 
#### Temperature (monthly average)
- Evaporation (monthly average)

Management inputs
- Carbon inputs to soil
- Farm Yard Manure
- DPM/RPM ratio

## Running RothC

### Equation 6:

$$ SOC_{bsl,i,t} = \int(SOC_{bsl,i,t}) $$

Where:
- $SOC_{bsl,i,t}$ = Estimated carbon stocks in the SOC pool in the baseline scenario for quantification unit i at the end of year t (tCO2e/ha)
- $\int(SOC_{bsl,i,t})$ = Modeled SOC stocks in the baseline scenario for quantification unit i in year t, calculated by modeling SOC stock changes over the course of the preceding year (tCO2e/ha)
- i = Quantification unit

# Error Analysis

## Equations 60-64: Analytical Error Propagation













