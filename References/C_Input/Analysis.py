import pandas as pd
import numpy as np
import csv

df = pd.read_csv("Ghana_Crop_Data.csv")
#print(df.head())
#print(df["DISTRICT"].unique())

def Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E):
	C_I = C_P * S_P + C_S * S_S + C_R * S_R + C_E * S_E
	return C_I

final_data = {'region':[], 'crop': [], 'yield': [], 'sem': [], 'moist_content':[], 'harvest_index':[], 'rs_ratio':[], 'carbon_input':[], 'baseline':[]}

# Static parameters
carbon_content = 0.45
root_exudate_ratio = 0.05 # of all other biomass

##########################
######### MAIZE ##########
##########################

crop = "MAIZE"
region = "UPPER WEST"
df = df[df["REGION"] == region]

print("All types of crops in dataset: ")
print(df["CROP"].unique())
print()

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)
sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std


print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.13
harvest_index = 0.48
rs_ratio = 0.1

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0
C_S = C_P * (1 - harvest_index)
S_S = 1
C_R = C_S * rs_ratio
S_R = 1
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

##########################
######### RICE ##########
##########################

df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "RICE"
df = df[df["REGION"] == region]


df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")

print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.13
harvest_index = 0.17
rs_ratio = 0.2

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0 
C_S = C_P * (1 - harvest_index)
S_S = 1 
C_R = C_S * rs_ratio
S_R = 1 
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1 

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

##########################
######### YAM ##########
##########################

df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "YAM"
region = "UPPER WEST"
df = df[df["REGION"] == region]


df = df[df["CROP"] == crop]      
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)
    
clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)    

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.7
harvest_index = 0.5
rs_ratio = 1 # not known, 1 is a placeholder

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0
C_S = C_P * (1 - harvest_index)
S_S = 1
C_R = 0
S_R = 1
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

##########################
######### SORGHUM ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "SORGHUM"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.12
harvest_index = 0.29
rs_ratio = 0.01

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0
C_S = C_P * (1 - harvest_index)
S_S = 1
C_R = C_S * rs_ratio
S_R = 1
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

##########################
######### MILLET ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "MILLET"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.12
harvest_index = 0.34
rs_ratio = 0.2

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0
C_S = C_P * (1 - harvest_index)
S_S = 1
C_R = C_S * rs_ratio
S_R = 1
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

##########################
######### GROUNDNUT ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "GROUNDNUT"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.10
harvest_index = 0.37
rs_ratio = 0.1

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0
C_S = C_P * (1 - harvest_index)
S_S = 1
C_R = C_S * rs_ratio
S_R = 1
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

##########################
######### COWPEA ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "COWPEA"
region = "UPPER WEST"
df = df[df["REGION"] == region]

df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.1
harvest_index = 0.23
rs_ratio = 0.1

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0
C_S = C_P * (1 - harvest_index)
S_S = 1
C_R = C_S * rs_ratio
S_R = 1
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

##########################
######### SOYABEAN ##########
##########################
df = pd.read_csv("Ghana_Crop_Data.csv")
crop = "SOYABEAN"
region = "UPPER WEST"
df = df[df["REGION"] == region]


df = df[df["CROP"] == crop]
#print(df)

# Converting mean values to integer type
yields_list = []

for value in df["YIELD (MT/HA)"]:
   value = float(str(value).strip())
   yields_list.append(value)

clean_list = [x for x in yields_list if not np.isnan(x)]

# Calculating mean and std
mean_value = np.mean(clean_list)
stdev_value = np.std(clean_list)

sem = np.std(clean_list, ddof=1) / np.sqrt(len(clean_list))  # ddof=1 uses sample std

print(f"Mean yield for {crop} in {region} region (mt/ha): {mean_value:.4f}")
print(f"Standard Error of Mean (mt/ha): {sem:.4f}")
print()

# Calculating C-input
crop_yield = mean_value
moist_content = 0.13
harvest_index = 0.34
rs_ratio = 0.09

C_P = (crop_yield - sem) * carbon_content * (1 - moist_content)
S_P = 0
C_S = C_P * (1 - harvest_index)
S_S = 1
C_R = C_S * rs_ratio
S_R = 1
C_E = (C_P + C_S + C_R) * (root_exudate_ratio / (1 - root_exudate_ratio))
S_E = 1

carbon_input = Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E)

final_data['region'].append(region)
final_data['crop'].append(crop)
final_data['yield'].append(mean_value)
final_data['sem'].append(sem)
final_data['moist_content'].append(moist_content)
final_data['harvest_index'].append(harvest_index)
final_data['rs_ratio'].append(rs_ratio)
final_data['carbon_input'].append(carbon_input)

burned = C_S*0.9
baseline = carbon_input - burned
final_data['baseline'].append(baseline)

################################

################################

print(final_data)

my_df = pd.DataFrame(final_data)
my_df.to_csv("output.csv", index=False)





