try:
    with  open('weather.dat') as f:
        lines = f.read().splitlines() #using this ensures we don't include line separators (\n) which come with f.readlines()
        # print(lines)

        spread, day = list(), list()

        #We start at index 2 where actual data starts and we get to the second last
        for i in range(2, len(lines)-1): 
            stripped_lines = lines[i].strip()

            # print(stripped_lines)

            #acreate array for ease of looping
            cols = stripped_lines.split()
            #print(cols)

            # try:
            #Cater for values without asterics
            if '*' not in cols[1] and '*' not in cols[2]:
                #get the difference
                diff = int(cols[1]) - int(cols[2])
                spread.append(diff)
                day += cols[0]

            #Cater for values with asterics in the MxT column
            elif '*' in cols[1]:
                cols[1] = cols[1][:-1]
                #print(cols[1])
                diff = int(cols[1]) - int(cols[2])
                spread.append(diff)
                day += cols[0]

            #Cater for values with asterics in the MnT column    
            elif '*' in cols[2]:
                cols[2] = cols[2][:-1]
                diff = int(cols[1]) - int(cols[2])
                spread.append(diff)
                day += cols[0]


    max_diff = max(spread)
    #print(max_diff)
    idx = spread.index(max_diff)
    res = day[idx] + " " + str(max_diff)
    print(res)
except:
    print('You do not have weather.dat file in your folder')