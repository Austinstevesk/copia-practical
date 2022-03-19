# Weather Data Solution  
  
# Running the code  
- Ensure you have weather.dat in the same folder as the weather.py script  
- Run the code using ```python weather.py```  

  
# Code Breakdown  
- Loading data we use ```with open``` since the data format is almost similar to text separated by spaces  
- To ensure we do not have ```\n``` in our lines, we use read().splitlines()  
- We then initialize a list to ensure we append data easily  
- Data will be appended in form of dictionary where the key is the Day(Dy) and the value is the spread(MxT-MnT)  
- We then removed spaces using ```lines[i].split```  
- ```splitted_lines.split``` ensures we create arrays for the different lines  
- We then check whether both the values (MxT and MnT) are ints and have no asterics -> We can perform the subration operations directly  
- We append the key, value pair to the list spread  
- We then remove asteric from the MxT column and perform the subtraction operation 
- We append the key, value pair to the list spread  
- We also remove the asteric from MnT column then perform the subtraction operation  
- We append the key, value pair to the list spread  
  
- Create empty lists to hold keys and values for the spread dictionaries (vals and keys)  
- We append all the items for the keys and values  
- We find maximum of the vals list  
- We get the index for the maximum value and use it to get the key  
- We concatinate the key and the value and return the list  
