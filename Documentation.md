
# SOC Sampling
FAO and IPCC best-practices were followed in soil sampling. The details on this section will be filled out soon.
## Equation 2: Minimum Detectable Difference
Details to be added, if necessary.
## Equation 3: Number of Samples
Details to be added, if necessary.
## Equation 4: SOC mass by depth layer


$$ M_{n,dl,SOC} = \frac{M_{n,dl,sample}}{\pi(\frac{D}{2})^2\times N} \times 10000  \times OC_{n,dl} $$

Where:

$M_{n,dl,SOC}$ = SOC mass in soil sample n in depth layer dl (kg/ha)

$M_{n,dl,sample}$ = Soil mass of sample n in depth layer dl (g)

$D$  = Inside diameter of probe or auger

$N$ = Number of cores sampled (unitless)

$OC_{n,dl}$ = Organic carbon content in sample n in depth layer dl (g/kg)

10000 = g/mm $^2$ to kg/ha

This equation is only required when comparing measured SOC from year to year, and is hence not relevant at this stage. However, SOC and bulk density data was collected in two depth layers as approved under VM0042, and SOC content was thus calculated separately for each depth layer, to ensure comparison on an ESM (Equivalent Soil Mass) basis.
# SOC Modeling
## Equation 5: SOC stocks

$$ SOC_{model} = 100 \times BD_{corr} \times OC_{n,dl} $$

Where:

$SOC_{model}$ = SOC stock as model input data (t/ha)

$BD_{corr}$ = Corrected bulk density of the fine soil fraction, after subtracting the mass proportion of the coarse fragments (g/cm $^3$ ) 
$d$ = Soil depth (cm)

100 = Conversion factor from g/cm $^2$ to t/ha


## Equation 6: Modeled SOC stocks

$$ SOC_{bsl,i,t} = \int(SOC_{bsl,i,t}) $$

Where:

$SOC_{bsl,i,t}$ = Estimated carbon stocks in the SOC pool in the baseline scenario for quantification unit i at the end of year t (tCO2e/ha)

$\int(SOC_{bsl,i,t})$ = Modeled SOC stocks in the baseline scenario for quantification unit i in year t, calculated by modeling SOC stock changes over the course of the preceding year (tCO2e/ha)

i = Quantification unit

# Error Analysis

## Equations 60-64: Analytical Error Propagation













