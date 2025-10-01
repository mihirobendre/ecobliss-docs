
def Bolinder_CI(C_P, S_P, C_S, S_S, C_R, S_R, C_E, S_E):
    C_I = C_P * S_P + C_S * S_S + C_R * S_R + C_E * S_E 
    return C_I 

final_data = {'region':[], 'crop': [], 'yield': [], 'sem': [], 'moist_content':[], 'rs_ratio':[], 'carbon_input':[]}

final_data['region'].append('UPPER WEST')
final_data['crop'].append('SORGHUM')

a = final_data['region']

print(a)

