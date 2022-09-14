# Scraping the Yahoo Finance
import requests # Python http for humans
from datetime import datetime # use for date and time
nr=i=0
# ticker names
ticker=["GOOG","AAPL","MSFT","AMZN","INTC","QCOM","COST","SNAP","BABA","NFLX"]
#instead of using an object, i went and used a huge list to link the names and values
#the index would be the value and stored there would be the name
tdata=[0] * 5000
data=[] #saves prices
subtotal=0
while nr < 10:
url = "https://finance.yahoo.com/quote/%s?p=%s" % (ticker[nr],ticker[nr]);
f = requests.get(url)
contents = f.text
nr += 1
i = contents.find('data-field="regularMarketPrice" data-trend="none"
data-pricehint="2" value="', i)
if i == -1:
break
# Find the 'Value' pre mark
start = contents.find('data-field="regularMarketPrice" data-trend="none"
data-pricehint="2"', i)
# Find the 'Value' post mark
end = contents.find('" active', i)
value = contents[start+76:end]
value=value.replace('&amp; ','')
data.append(value)
tdata[int(float(value))] = ticker[nr-1]
# Found name + title ? => display
if len(ticker)>0 and len(value)>0:
string = "%d) %s = $%s " % (nr,ticker[nr-1],value);
print(string)
#print('=' * len(string))
i += 1
print("=============================================")
string = "Before sort: %s = $%s ... %s = $%s" %
(ticker[0],data[0],ticker[9],data[9]);
print(string)
data.sort(key = float, reverse = True)
string = "After sort: %s = $%s ... %s = $%s" %
(tdata[int(float(data[0]))],data[0],tdata[int(float(data[9]))],data[9]);
print(string)
print("=============================================")
diff=nr=0
while nr < 10:
total=i=0
while total < (10000+diff): #calculate for specific budgets
total = float(data[nr]) * i
i += 1
diff = 10000-total #calculate difference left for next run
subtotal += total
string = "%d) %s %d x $%s = %.2f " %
(nr+1,tdata[int(float(data[nr]))],(i-1),data[nr],total)
print(string)
nr += 1
print("=============================================")
string = "Total Account value = %.2f" % subtotal
print(string)
now = datetime.now()
string = now.strftime("%m/%d/%Y %H:%M:%S")
print("on ", string)
