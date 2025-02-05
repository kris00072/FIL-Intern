price_list=[100,90,70,110,120,60,200,95,135];
gst=17;
newPriceList=[];

for i in price_list:
    if(i>100):
        newPriceList.append(i+(i*gst/100));
    else:
        newPriceList.append(i);

print(newPriceList);