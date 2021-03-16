
import re
import pandas as pd


# Settings GitHub Path: 
url2 = 'https://github.com/gcsilva83/MetObjectsEdit/blob/main/df_etl.pkl?raw=true'
# Loading file
Met_Obj = pd.read_pickle(url2)


ObjectID = int(input("Object ID: "))
    # print("Object ID: " + ObjectID)
    #if to check if object id is numeric .isdigit() or .isnumeric()
    
dimensions = input("Enter dimensions: ")
    # print("dimensions is: " + dimensions)

def does_it_fit(ObjectID,dimensions):

    dim_list = re.findall(r'\d+', dimensions)
    #error with float numbers
    #print(dim_list)
    List_length = len(dim_list)
    #print ("Number of items in the list = ",len(dim_list))
    a =  int(dim_list[ 0])
    b =  int(dim_list[-1])
    c =  int(dim_list[-2])

    #if to avoid when a item has only one measure
    query = Met_Obj.query('Object_ID == @ObjectID')
    H1 = query['H1'].astype(str).astype(float).iloc[0]
    W1 = query['W1'].astype(str).astype(float).iloc[0]
    D1 = query['D1'].astype(str).astype(float).iloc[0]
    res_0 = [ H1,W1,D1]
    print ("The dimensions of the selected object are : " +  str(res_0))
   ## add error check when the object id is not found

        
    if List_length == 1:
      if H1 <= a : 
       return print("True") 
      else:
          print("False")
    elif List_length == 2:
         if H1 <= a and W1 <= b : 
            return  print("True")
         else:
          print("False")

    elif List_length == 3:
        if H1 <= a and W1 <= b and D1 <= c: 
          return  print("True")
        else:
          print("False")
    else:
        return print("False")


does_it_fit(ObjectID, dimensions)



