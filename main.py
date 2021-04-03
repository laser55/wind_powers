all_turbines = 25
turbine_power = 0
sum_power = 0
turbine_counter  = 1

while turbine_counter <= all_turbines:
    if turbine_counter <11:
        turbine_power = 2000
        sum_power += turbine_power
        print ("A(z) " + str(turbine_counter) + ". számú szélturbina teljes fordulaton működik, 2000 MWh-t termelve. A farmon termelt összenergia jelenleg " + str(sum_power) + " MWh.")    
        

    elif turbine_counter < 21:
        turbine_power = 1000
        sum_power += turbine_power
        print ("A(z) " + str(turbine_counter) + ". számú szélturbina fél fordulaton működik, 1000 MWh-t termelve. A farmon termelt összenergia jelenleg " + str(sum_power) + " MWh.")

    else: 
        turbine_power = 0
        sum_power += turbine_power
        print ("A(z) " + str(turbine_counter) +  ". számú szélturbina nem működik, 0 MWh-t termelve. A farmon termelt összenergia jelenleg " + str(sum_power) + " MWh.")

    turbine_counter += 1

