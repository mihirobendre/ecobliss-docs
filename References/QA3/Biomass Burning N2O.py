import pandas as pd

# --------------------------------------------------------------------------------------------------
# Python Script: N₂O Emissions from Biomass Burning (VM0042 v2.1 Equations 33 & 59)
# --------------------------------------------------------------------------------------------------

# ----------------------------
# 1. SITE-SPECIFIC INPUTS (EDITABLE)
# ----------------------------

# Biomass burned in the baseline scenario (MB_bsl,c,i,t) [t dry matter per hectare]
# >> Should be measured on-site or taken from local field studies.
# >> Example default: 5.5 t DM/ha for agricultural residues (IPCC 2006 GL Vol 4, Ch 2, Table 2.4).
MB_bsl = 0.124171426/0.45  # t DM/ha

# Combustion completeness factor (CF_c) [unitless fraction]
# >> Fraction of above-ground biomass actually combusted in fire.
# >> Should be measured or estimated from local fire behavior, due to no measurements ICC default used
# >> Typical IPCC default for residues: 0.9.
CF = 0.755  # unitless  average between early/mid/late season burns in savannah grasslands

# N₂O emission factor (EF_c,N2O) [g N₂O per kg dry matter burned]
# >> From IPCC 2006 GL Vol 4, Ch 2, Table 2.5 (Andreae & Merlet, 2001).
EF_N2O = 0.21  # g/kg DM

# Area of burned land (A_i) [ha]
# >> Project-specific area under burning.
area_ha = 18200  # ha

# Global Warming Potential for N₂O (GWP_N2O)
# >> IPCC AR6 WGI Table 7.15: 100‑yr GWP including climate-carbon feedbacks.
# >> See: https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7 (#Table7.15)
GWP_N2O = 273  # unitless

# ----------------------------
# 2. EQUATION 33: CALCULATE AREAL MEAN N₂O EMISSIONS (t CO₂e/ha)
#    N2O_bbbsl_i_t_ha = [GWP_N2O × (MB_bsl × 1000 kg/t × EF_N2O g/kg × CF)] / 10^6 g→t
#    Simplified: = GWP_N2O × MB_bsl × CF × EF_N2O / 1000
# ----------------------------

# Convert N₂O emissions to t CO2e per ha
n2o_co2e_per_ha = (GWP_N2O * MB_bsl * CF * EF_N2O) / 1000

# ----------------------------
# 3. EQUATION 59: SCALE TO TOTAL AREA TO GET TOTAL EMISSIONS (t CO₂e)
#    ΔN2O_bbt = (N2O_bbbsl_i_t_ha - N2O_bbwp_i_t_ha) × A_i
#    Here N2O_bbwp_i_t_ha is project scenario; assume zero or manually input below.
# ----------------------------

# Project scenario N2O emissions per ha [t CO₂e/ha]
# >> If project burning occurs, input analogous MB_prj and CF_prj; else zero.
n2o_co2e_prj_per_ha = 0.0  # t CO₂e/ha

# Total baseline emissions
total_n2o_co2e_baseline = n2o_co2e_per_ha * area_ha

# Total project emissions
total_n2o_co2e_project = n2o_co2e_prj_per_ha * area_ha

# Emission reduction achieved
total_n2o_reduction = total_n2o_co2e_baseline - total_n2o_co2e_project

# ----------------------------
# 4. OUTPUT RESULTS IN A PANDA DATAFRAME
# ----------------------------

df_results = pd.DataFrame([{
    'Variable': 'MB_bsl (t DM/ha)',
    'Value': MB_bsl,
    'Units': 't DM/ha',
    'Source': 'Project site measurement or IPCC 2006 GL Vol4, Ch2, Table2.4'
}, {
    'Variable': 'CF (combustion completeness)',
    'Value': CF,
    'Units': 'fraction',
    'Source': 'Project site measurement or IPCC 2006 GL defaults'
}, {
    'Variable': 'EF_N2O (g N₂O/kg DM)',
    'Value': EF_N2O,
    'Units': 'g/kg',
    'Source': 'IPCC 2006 GL Vol4, Ch2, Table2.5 (Andreae & Merlet 2001)'
}, {
    'Variable': 'GWP_N2O',
    'Value': GWP_N2O,
    'Units': 'unitless (273)',
    'Source': 'IPCC AR6 WGI, Table 7.15'
}, {
    'Variable': 'n2o_co2e_per_ha',
    'Value': round(n2o_co2e_per_ha, 6),
    'Units': 't CO₂e/ha',
    'Source': 'Equation 33 (VM0042 v2.1)'
}, {
    'Variable': 'area_ha',
    'Value': area_ha,
    'Units': 'ha',
    'Source': 'Project site'
}, {
    'Variable': 'total_n2o_co2e_baseline',
    'Value': round(total_n2o_co2e_baseline, 3),
    'Units': 't CO₂e',
    'Source': 'Equation 59 (VM0042 v2.1)'
}, {
    'Variable': 'total_n2o_co2e_project',
    'Value': round(total_n2o_co2e_project, 3),
    'Units': 't CO₂e',
    'Source': 'Equation 59 (VM0042 v2.1)'
}, {
    'Variable': 'total_n2o_reduction',
    'Value': round(total_n2o_reduction, 3),
    'Units': 't CO₂e',
    'Source': 'Difference between baseline & project (Eq 59)'
}])

# Display the results
print(df_results)

