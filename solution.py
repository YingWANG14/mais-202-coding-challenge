
import csv
import numpy as np
import matplotlib.pyplot as plt

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #create a dictionary with purposes as keys and the lists of corresponding interest rates as values
    dic = {}
    for row in readCSV:
        purpose = row[16]
        #First line is useless
        if purpose == "purpose":
            continue
        #If there doesn't exist this purpose, create a new pair with this new purpose as the key
        if dic.get(purpose) is None:
            rates = []
            dic[purpose] = rates
            rates.append(float(row[5]))
        #If there exist this purpose, append its corresponding interest rate list
        else:
            dic[purpose].append(float(row[5]))

    #Calculate the corresponding average interest rates for each purpose
    for key in dic:
        avg_rate = sum(dic[key])/len(dic[key])
        dic[key] = avg_rate

    #Sort the pairs alphabetically by keys
    pur_list=dic.keys()
    pur_list.sort()
    int_list=[]
    text=[]
    for pur in pur_list:
        int_list.append(dic[pur])
        text.append([pur,'%.3f'%dic[pur]])

    #Create a table
    fig = plt.figure(figsize=(20,5))
    ax = plt.subplot2grid((5,12), (0,0), colspan=3)
    col_label=('purpose','avg_rate')
    table=ax.table(cellText=text,colLabels=col_label,loc='upper left')
    ax.axis("off")

    #Plot the reslut to a bar chart
    plt.subplot2grid((5,12), (0,4),colspan=9,rowspan=3)
    left = np.arange(len(dic))
    height = int_list
    color_list=['rosybrown','gold','skyblue','plum','coral','slateblue',
        'pink','orange','lightseagreen','slategrey','g','c']
    plt.bar(left,height,color=color_list,align='center')

    plt.xlabel('purpose')
    plt.ylabel('mean(int_rate)')
    plt.xticks(left,pur_list,fontsize=7)
    plt.yticks(np.arange(0, 20, 2.5),fontsize=6)
    plt.title('loan rate')


    plt.show()






