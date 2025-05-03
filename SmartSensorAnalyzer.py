# Breaife about the author:
# Name: Tarek Adel Ali
# Task: 04
# Compant: Kaitech


# original data
sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
]


###################################################################################################################
# Organize readings per sensor
def organize_readings(sensor_data):
    reading_sensor={}
    for sensor in sensor_data:
        sensor_id, timestamp, temperature, stress, displacement = sensor
        if sensor_id not in reading_sensor:
            reading_sensor[sensor_id]=[]
        reading_sensor[sensor_id].append({"timestamp":timestamp, "temperature":temperature,"stress": stress, "displacement":displacement})
    return reading_sensor

def show_data_before_and_after(original_data, organized_data):
    
    print("Data before organizing:")
    print(original_data)
    print("\nData after organizing:")
    print(organized_data)



#####################################################################################################################


# Identify unique sensors with extreme values
def Extreme_sensors(data):
    max_temp = float('-inf')  #save maximum temperature
    min_temp = float('inf')   #save minimum temperature
    max_temp_sensor = 0   #save sensor id with maximum temperature
    min_temp_sensor = 0 #save sensor id with minimum temperature

# for loop to find the sensor with maximum and minimum temperature
    for  sensor_id,readings in data.items():
        for reading in readings:
            if reading["temperature"] > max_temp:
                max_temp = reading["temperature"]
                max_temp_sensor = sensor_id
            if reading["temperature"] < min_temp:
                min_temp = reading["temperature"]
                min_temp_sensor = sensor_id
    print(f"Sensor with max temperature: {max_temp_sensor} with extreme value in temperature: {max_temp}℃")
    print(f"Sensor with min temperature: {min_temp_sensor} with extreme value in temperature: {min_temp}℃")



###########################################################################################################################
#Compare readings from different time intervals
def Compare_readings(data):
    for sensor_id, readings in data.items():
        if len(readings) < 2:
            print(f"Sensor {sensor_id} has one time reading which is {readings[0]['temperature']}℃ at {readings[0]['timestamp']}")
            continue
        for i in range(len(readings)-1):
            current_reading = readings[i]
            next_reading=readings[i+1]
            temp_diff = next_reading["temperature"] - current_reading["temperature"]
            stress_diff = next_reading["stress"] - current_reading["stress"]
            if temp_diff > 0:
                print(f"Sensor {sensor_id} has a temperature increased of {abs(temp_diff):.2f} between {current_reading['timestamp']} and {next_reading['timestamp']}")
            elif temp_diff < 0:
                print(f"Sensor {sensor_id} has a temperature decreased of {abs(temp_diff):.2f} between {current_reading['timestamp']} and {next_reading['timestamp']}")
            else:
                print(f"Sensor {sensor_id} has a constant temperature between {current_reading['timestamp']} and {next_reading['timestamp']}")



########################################################################################################################################


#Summarize the data by calculating max, min, and average readings per sensor
#Calculate statistics per sensor
def Summarize_data(data):
    print("Which data do you want to show?")
    print("1. Temperature")
    print("2. Stress")
    print("3. Displacement")
    print("4. All")
    choice = input("Enter your choice (1-4): ")
    for sensor_id, readings in data.items():
        temperatures=[]
        for r in readings:  # traditional way to extract temperature values and store them in a list
             temperatures.append(r["temperature"])
        stress=[r["stress"] for r in readings] # modern way to extract stress values and store them in a list
        displacements=[r["displacement"] for r in readings] # store displacements in a list
        temp_max=max(temperatures) # find maximum temperature
        temp_min=min(temperatures) # find minimum temperature
        tem_avg=sum(temperatures)/len(temperatures) # find average temperature
        stress_max=max(stress) # find maximum stress
        stress_min=min(stress) # find minimum stress
        stress_avg=sum(stress)/len(stress) # find average stress
        displacement_max=max(displacements) # find maximum displacement
        displacement_min=min(displacements) # find minimum displacement
        displacement_avg=sum(displacements)/len(displacements) # find average displacement
        # Print the statistics for each sensor
        print(f"\nSensor {sensor_id} has the following statistics:")
        if choice == "1":
            print(f"Max temperature: {temp_max:.2f}℃ and min temperature: {temp_min:.2f} and average temperature: {tem_avg:.2f}")
        elif choice == "2":
            print(f"Max stress: {stress_max:.2f} and min stress: {stress_min:.2f} and average stress: {stress_avg:.2f}")
        elif choice == "3":
            print(f"Max displacement: {displacement_max} and min displacement: {displacement_min} and average displacement: {displacement_avg}")
        elif choice == "4":
            print(f"Max temperature: {temp_max:.2f}℃ and min temperature: {temp_min:.2f} and average temperature: {tem_avg:.2f}")
            print(f"Max stress: {stress_max:.2f} and min stress: {stress_min:.2f} and average stress: {stress_avg:.2f}")
            print(f"Max displacement: {displacement_max} and min displacement: {displacement_min} and average displacement: {displacement_avg}")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            return 0
        


################################################################################################################################

#Group data by sensor using a dictionary (sensor_id as key, list of tuples as value)
def Group_data_by_sensor(original_data):
    print("Before grouping:")
    print(original_data)
    grouped_data = {}
    for sensor_id, timestamp, temperature, stress, displacement in original_data:
        if sensor_id not in grouped_data:
            grouped_data[sensor_id] = []
        grouped_data[sensor_id].append((timestamp, temperature, stress, displacement))
    #show the new data structure
    for sensor_id, readings in grouped_data.items():
        print(f"\nSensor {sensor_id} has the following readings:")
        for reading in readings:
            print(f"Timestamp: {reading[0]}, Temperature: {reading[1]}℃, Stress: {reading[2]}, Displacement: {reading[3]}")
    print("\nAfter grouping:")
    print(grouped_data)
###############################################################################################################################

#Use sets to find unique sensor IDs that recorded stress > 13.0
def unique_sensor_set(original_data):
    unique_sensor=set() 
    for sensor_id, _, _, stress, _ in original_data:
        if stress > 13.0:
            unique_sensor.add(sensor_id)
    print(f"{unique_sensor.pop()} has a stress value greater than 13.0")
    


################################################################################################################################

#Max, min, and average temperature
#Max displacement
def max_and_min_values(data):
    max_temp = float('-inf')  #save maximum temperature
    min_temp = float('inf')   #save minimum temperature
    avg_temp = 0 #save average temperature
    max_displacement = float('-inf') #save maximum displacement
    # for loop to find the sensor with maximum and minimum temperature
    for  sensor_id,readings in data.items():
        for reading in readings:
            if reading["temperature"] > max_temp:
                max_temp = reading["temperature"]
            if reading["temperature"] < min_temp:
                min_temp = reading["temperature"]
            if reading["displacement"] > max_displacement:
                max_displacement = reading["displacement"]
            if reading["temperature"] > 0:
                avg_temp += reading["temperature"]
    avg_temp /= len(sensor_data) # calculate average temperature
    print(f"The maximum temperature is {max_temp}℃ and the minimum temperature is {min_temp}℃ and the average temperature is {avg_temp:.2f}℃")
    print(f"The maximum value in displacement: {max_displacement}m")



################################################################################################################################################


#Extract all timestamps into a list and sort them
def timestapms_extracted(data):
    print("You want all timestamps? or you want witout duplicates?")
    print("1. All timestamps")
    print("2. Timestamps without duplicates")
    choice = input("Enter your choice (1-2): ")
    timestamps = []
    for readings in data.values():
        for reading in readings:
            timestamps.append(reading["timestamp"])
    if choice == "1": ## Sort the timestamps
        timestamps = sorted(timestamps)  
    elif choice == "2": ## Remove duplicates and sort the timestamps
        timestamps = sorted(set(timestamps))
    else:
        print("Invalid choice. Please enter a number between 1 and 2.")
    
    print(f"Sorted timestamps: {timestamps}")## Print the sorted timestamps





########################################################################################################################################


#Create a tuple of the most recent reading for each sensor
def most_recent_reading(data):
    recent_readings = tuple() # Create an empty tuple to store the most recent readings
    for sensor_id, readings in data.items():
        if readings:
            most_recent = readings[-1] # Get last reading for each sensor
            recent_readings += (sensor_id, most_recent["timestamp"], most_recent["temperature"], most_recent["stress"], most_recent["displacement"])
    print(recent_readings) # Print the tuple of most recent readings for each sensor



########################################################################################################################################


#Main function to call all the functions
def main():
    reading_sensor = organize_readings(sensor_data)  # Organize the data
    print("Welcome to the sensor data analysis program!")
    print("Please choose an option:")
    print("1. Organize readings per sensor")
    print("2. Identify unique sensors with extreme values")
    print("3. Compare readings from different time intervals")
    print("4. Summarize the data by calculating max, min, and average readings per sensor")
    print("5. Group data by sensor using a dictionary (sensor_id as key, list of tuples as value)")
    print("6. Use sets to find unique sensor IDs that recorded stress > 13.0")
    print("7. Calculate statistics per sensor")
    print("8. Max, min, and average temperature and max displacement")
    print("9. Extract all timestamps into a list and sort them")
    print("10. Create a tuple of the most recent reading for each sensor")
    print("11. Exit")
    choice = input("Enter your choice (1-11): ")
    if choice == "1":
        show_data_before_and_after(sensor_data, reading_sensor)
    elif choice == "2":
        Extreme_sensors(reading_sensor)
    elif choice == "3":
        Compare_readings(reading_sensor)
    elif choice == "4":
        Summarize_data(reading_sensor)
    elif choice == "5":
        Group_data_by_sensor(sensor_data)
    elif choice == "6":
        unique_sensor_set(sensor_data)
    elif choice == "7":
        Summarize_data(reading_sensor)
    elif choice == "8":
        max_and_min_values(reading_sensor)
    elif choice == "9":
        timestapms_extracted(reading_sensor)
    elif choice == "10":
        most_recent_reading(reading_sensor)
    elif choice == "11":
        print("Exiting the program.")       
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

while True:
    main()
    cont = input("Do you want to continue? (y/n): ").strip().lower()
    if cont != "y":
        print("Exiting the program.")
        break
