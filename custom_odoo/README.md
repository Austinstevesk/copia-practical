# Odoo Custom Modules  
  
Question -> 3,5  
  
# Module Details   
   
# Installation  

# Vehicle Module
- vehicle_details  
- This incudes the vehicle details and C-Track-Data  
  
- Clone the repository, copy vehicle_details module to odoo/custom/addons  
- Restart odoo using ```sudo service odoo-server restart```  
- Get to the UI and search for the module ```vehicle_details``` then install  
- Upgrade the module  
- Get to the module and you will have a list view  
- In the List View, I have limited the features since you cannot view everything  
- Click edit and get to Form view  
- Add the details and save  

# Custom_partner module (For the customers)
- This includes the custom_partner module to add children fields  
  
- Clone the repository, copy custom_partners module to odoo/custom/addons  
- Restart odoo using ```sudo service odoo-server restart```  
- Get to the UI and search for the module ```custom_partners``` then install  
- Upgrade the module  
- Get to sales app and click on Sales -> Orders -> Customers and click on one customer 
- Click edit   
- The details will be available as per the description -> select Has Children as ```Yes```  
- Save the data after filling in details  
- Note: You cannot add more children details than the number specified  