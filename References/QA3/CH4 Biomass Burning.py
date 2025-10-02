# Methane Emissions from Biomass Burning (CH4_bbsl) - VM0042 v2.1 Equations 15 and 57
# Version with Detailed Notes and Crop-Specific Transparency

# ------------------------------------------------------------------
# 📘 BACKGROUND
# Equation (15) – Baseline Areal CH₄ Emissions:
# CH4_bbsl = (GWP_CH4 × ∑ (MB_c × CF_c × EF_c,CH4)) / (1,000,000 × A)

# Equation (57) – Emissions Reductions:
# ΔCH4_bbt = (CH4_bbsl - CH4_bbwp) × A

# All emission factors and combustion factors are from:
# 🔗 IPCC 2019 Refinement to the 2006 Guidelines
# Volume 4, Chapter 2, Table 2.5:
# https://www.ipcc-nggip.iges.or.jp/public/2019rf/pdf/4_Volume4/19R_V4_Ch02_Generic%20Methods.pdf

# Global Warming Potential (100-year) from:
# 🔗 IPCC AR5:
# https://ghgprotocol.org/sites/default/files/Global-Warming-Potential-Values%20%28Feb%2016%202016%29_1.pdf

# All values are editable and clearly labeled below
# ------------------------------------------------------------------

# ------------------------------
# INPUT PARAMETERS (EDITABLE)
# ------------------------------

# IPCC AR5 100-year Global Warming Potential for CH4
GWP_CH4 = 28  # t CO2e / t CH4

# Total project area (hectares)
A = 18200

# Project scenario CH4 emissions from burning (set to 0 if avoided)
CH4_bbwp = 0  # t CO2e/ha

crop_breakdown = {"Cereals": 0.6, "Legumes": 0.3, "Roots": 0.1}
cereals_breakdown = {"Maize":0.7, "Sorghum":0.15, "Millet": 0.05, "Rice":0.15}
legumes_breakdown = {"Groundnut": 0.5, "Cowpea": 0.2, "Soyabean":0.25, "Bambara":0.05}
root_breakdown = {"Yam": 0.7, "Sweet Potato": 0.3}

# Residue data dictionary — includes crop-specific IPCC default values
# All crops listed here are common in Ghana and West Africa
residue_data = {
    "Maize": {
        "MB_c": 0.101420647/0.45 * 1000 * A * crop_breakdown["Cereals"] * cereals_breakdown["Maize"],       # Mass of maize residues burned (kg dry matter)
        "CF_c": 1.0,        # Combustion factor, IPCC Table 2.5 (default for cereal residues)
        "EF_c_CH4": 2.7     # CH4 emission factor (g CH4/kg dry matter)
    },

	"Rice": {
		"MB_c": 0.195344543/0.45 * 1000 * A* crop_breakdown["Cereals"] * cereals_breakdown["Rice"],
		"CF_c": 1.0,
		"EF_c_CH4":2.7
		},
	
    "Yam": {
        "MB_c": 0.24717298/0.45 * 1000 * A* crop_breakdown["Roots"] * root_breakdown["Yam"],
        "CF_c": 1.0,
        "EF_c_CH4":2.7
        },

    "Sweet Potato": {
        "MB_c": 0.24717298/0.45 * 1000 * A* crop_breakdown["Roots"] * root_breakdown["Sweet Potato"],
        "CF_c": 1.0,
        "EF_c_CH4":2.7
        },  

    "Sorghum": {
        "MB_c": 0.06633039/0.45 * 1000 * A* crop_breakdown["Cereals"] * cereals_breakdown["Sorghum"],
        "CF_c": 1.0,
        "EF_c_CH4":2.7
        },

    "Millet": {
        "MB_c": 0.100274341/0.45 * 1000 * A* crop_breakdown["Cereals"] * cereals_breakdown["Millet"],
        "CF_c": 1.0,
        "EF_c_CH4": 2.7
    },

    "Groundnut": {
        "MB_c": 0.114137561/0.45 * 1000 * A* crop_breakdown["Legumes"] * legumes_breakdown["Groundnut"],
        "CF_c": 1.0,
        "EF_c_CH4": 2.7
    },

    "Cowpea": {
        "MB_c": 0.08920197/0.45 * 1000 * A* crop_breakdown["Legumes"] * legumes_breakdown["Cowpea"],
        "CF_c": 1.0,
        "EF_c_CH4": 2.7
	},

    "Soyabean": {
        "MB_c": 0.08695255/0.45 * 1000 * A* crop_breakdown["Legumes"] * legumes_breakdown["Soyabean"],
        "CF_c": 1.0,
        "EF_c_CH4": 2.7
	},

    "Bambara": {
        "MB_c": 0.08695255/0.45 * 1000 * A* crop_breakdown["Legumes"] * legumes_breakdown["Bambara"],
        "CF_c": 1.0,
        "EF_c_CH4": 2.7
    }

}

# ------------------------------
# CONSTANTS
# ------------------------------
g_to_tonne = 1e-6  # Conversion from grams to tonnes

# ------------------------------
# CALCULATION LOGIC
# ------------------------------
total_CH4_emissions_t = 0  # Total emissions (tonnes CO2e)
detailed_output = []       # Collects individual crop calculations

for crop, values in residue_data.items():
    MB = values["MB_c"]           # Mass of dry biomass burned (kg)
    CF = values["CF_c"]           # Combustion factor (dimensionless)
    EF = values["EF_c_CH4"]       # Emission factor (g CH4/kg dry matter)

    # Calculate emissions in grams of CH4
    emissions_CH4_g = MB * CF * EF

    # Convert g CH4 → tonnes CH4 → t CO2e
    emissions_CH4_t = emissions_CH4_g * g_to_tonne
    emissions_CO2e = emissions_CH4_t * GWP_CH4

    # Accumulate total emissions
    total_CH4_emissions_t += emissions_CO2e

    # Store detailed breakdown
    detailed_output.append({
        "Crop": crop,
        "Mass Burned (kg)": MB,
        "Combustion Factor (CF)": CF,
        "EF_CH4 (g/kg)": EF,
        "CH4 Emissions (t)": round(emissions_CH4_t, 6),
        "CH4 Emissions (t CO2e)": round(emissions_CO2e, 4)
    })

# Areal mean baseline emissions
CH4_bbsl = total_CH4_emissions_t / A  # t CO2e/ha

# Emission reductions (if burning is avoided)
delta_CH4_bbt = (CH4_bbsl - CH4_bbwp) * A  # t CO2e

# ------------------------------
# OUTPUT
# ------------------------------
import pandas as pd

# Create output DataFrame
df_output = pd.DataFrame(detailed_output)

# Add totals row
df_output.loc[len(df_output.index)] = {
    "Crop": "TOTAL",
    "Mass Burned (kg)": "",
    "Combustion Factor (CF)": "",
    "EF_CH4 (g/kg)": "",
    "CH4 Emissions (t)": round(total_CH4_emissions_t / GWP_CH4, 6),
    "CH4 Emissions (t CO2e)": round(total_CH4_emissions_t, 4)
}

# Print the full table
print("\nDetailed CH4 Emissions from Biomass Burning by Crop:\n")
print(df_output.to_string(index=False))

# Print final emission summary
print("\nSummary:")
print(f"Areal CH₄ Emissions in Baseline (t CO₂e/ha): {round(CH4_bbsl, 4)}")
print(f"Total CH₄ Emission Reductions (t CO₂e): {round(delta_CH4_bbt, 4)}")
