ward_1 = [
    {'name': 'Tunde', 'age': 31, 'temperature': 38.5},
    {'name': 'Chidi', 'age': 19, 'temperature': 36.6}
]

new_patient = {'name': 'Amaka', 'age': 24, 'temperature': None}
ward_1.append(new_patient)

while True:
    print('\n--- CLINICAL DASHBOARD ---')
    print('1. Scan current ward')
    print('2. Register new patient')
    print('3. Exit system')
    
    choice = input('Select an option (1-3): ')
    
    if choice == '3':
        print('Shutting down. Goodbye!')
        break
        
    elif choice == '1':
        print('\n--- SCANNING WARD RECORDS ---')
        for patient in ward_1:
            temp = patient['temperature']
            name = patient['name']
            
            if temp is not None:
                if temp > 38.5:
                    print(name + ' has a CRITICAL fever 🚨')
                elif temp > 37.5:
                    print(name + ' has a mild fever ⚠️')
                elif temp >= 35.0:
                    print(name + ' is stable ✅')
                elif temp < 35.0:
                    print(name + ' has Hypothermia 🥶')
            else:
                print('ERROR: ' + name + ' patient data unavailable ❌')
                
    elif choice == '2':
        print('\n--- REGISTER NEW PATIENT ---')
        new_name = input('Enter Name: ')
        new_age = int(input('Enter age: '))
        raw_temp = input('Enter temp (or leave blank if missing): ')
        
        if raw_temp == '':
            new_temp = None
        else:
            new_temp = float(raw_temp)
            
        added_patient = {'name': new_name, 'age': new_age, 'temperature': new_temp}
        ward_1.append(added_patient)
        print(new_name + ' successfully added to the ward list!')
        
    else:
        print('Invalid choice. Please select 1, 2, or 3.')
