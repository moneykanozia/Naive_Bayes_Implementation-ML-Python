import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('ML_DataSet.csv')
d = {'weather':[],'temp':[],'humidity':[],'windy':[],'yes':[],'no':[],'p':[]}
for i in ['sunny','overcast','rainy']:
	for j in ['hot','mild','cool']:
		for k in ['high','normal']:
			for l in [True,False]:
				d['weather'].append(i)
				d['temp'].append(j)
				d['humidity'].append(k)
				d['windy'].append(l)
				d['yes'].append(0)
				d['no'].append(0)
				d['p'].append(0)

data2 = pd.DataFrame(d)
def setData2YesAndNo(weather,temp,humidity,windy,play,length):
	for i in range(len(data2)):
		if data2.loc[i,'weather']==weather:
			if data2.loc[i,'temp']==temp:
				if data2.loc[i,'humidity']==humidity:
					if data2.loc[i,'windy']==windy:
						if play=='yes':
							data2.loc[i,'yes']+=length
						elif play=='no':	
							data2.loc[i,'no']+=length	
for i in ['sunny','overcast','rainy']:
	for j in ['hot','mild','cool']:
		for k in ['high','normal']:
			for l in [True,False]:
				for m in ['yes','no']:
					length = len(data[(data['weather']==i)&(data['temp']==j)&(data['humidity']==k)&(data['windy']==l)&(data['play']==m)])	
					setData2YesAndNo(i,j,k,l,m,length)
for i in range(len(data2)):
	data2.loc[i,'p']=(data2.loc[i,'yes']+data2.loc[i,'no'])/((data2['yes'].sum())+(data2['no'].sum()))
p_Yes=(data2['yes'].sum())/((data2['yes'].sum())+(data2['no'].sum()))
p_No=(data2['no'].sum())/((data2['yes'].sum())+(data2['no'].sum()))
# print(data2)
w=input('enter the weather')
t=input('enter the temprature')
h=input('enter the humidity')
wn=input('enter the windy')	
p_combinYes=(data2[(data2['weather']==w) & (data2['temp']==t) & (data2['humidity']==h) & (data2['windy']==bool(wn))]['yes'].values[0])/data2['yes'].sum()
p_combin=data2[(data2['weather']==w) & (data2['temp']==t) & (data2['humidity']==h) & (data2['windy']==bool(wn))]['p'].values[0]
result=(p_combinYes*p_Yes)/p_combin
print(result)
plt.gca().set_position([0.2,0.1,0.1,0.8])
plt.bar(0, result, align = "edge")
plt.title("-")
plt.xlabel("-")
plt.ylabel("percent")
plt.ylim(0,1)
plt.xticks([]) # remove x ticks
plt.yticks([0,0.25,0.50,0.75,1])
plt.margins(0) # remove extra whitespace
plt.show()


# print(data2)					
# for i in range(len(data)):
# 	if data.loc[i,'weather']=='sunny':
# 		if data.loc[i,'temp']=='hot':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','hot','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','hot','high',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','hot','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','hot','high',False,'no')	
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','hot','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','hot','normal',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','hot','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','hot','normal',False,'no')		
# 		elif data.loc[i,'temp']=='mild':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','mild','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','mild','high',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','mild','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','mild','high',False,'no')		
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','mild','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','mild','normal',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','mild','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','mild','normal',False,'no')		
# 		elif data.loc[i,'temp']=='cool':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','cool','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','cool','high',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','cool','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','cool','high',False,'no')			
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','cool','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','cool','normal',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('sunny','cool','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('sunny','cool','normal',False,'no')					
# 	elif data.loc[i,'weather']=='overcast':
# 		if data.loc[i,'temp']=='hot':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','hot','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','hot','high',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','hot','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','hot','high',False,'no')	
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','hot','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','hot','normal',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','hot','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','hot','normal',False,'no')		
# 		elif data.loc[i,'temp']=='mild':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','mild','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','mild','high',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','mild','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','mild','high',False,'no')		
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','mild','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','mild','normal',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','mild','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','mild','normal',False,'no')		
# 		elif data.loc[i,'temp']=='cool':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','cool','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','cool','high',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','cool','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','cool','high',False,'no')			
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','cool','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','cool','normal',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('overcast','cool','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('overcast','cool','normal',False,'no')	
# 	elif data.loc[i,'weather']=='rainy':
# 		if data.loc[i,'temp']=='hot':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','hot','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','hot','high',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','hot','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','hot','high',False,'no')	
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','hot','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','hot','normal',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','hot','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','hot','normal',False,'no')		
# 		elif data.loc[i,'temp']=='mild':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','mild','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','mild','high',True,'no')	
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','mild','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','mild','high',False,'no')		
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','mild','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','mild','normal',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','mild','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','mild','normal',False,'no')		
# 		elif data.loc[i,'temp']=='cool':
# 			if data.loc[i,'humidity']=='high':
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','cool','high',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','cool','high',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','cool','high',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','cool','high',False,'no')			
# 			elif data.loc[i,'humidity']=='normal':		
# 				if data.loc[i,'windy']==True:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','cool','normal',True,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','cool','normal',True,'no')		
# 				elif data.loc[i,'windy']==False:
# 					if data.loc[i,'play']=='yes':
# 						setData2YesAndNo('rainy','cool','normal',False,'yes')
# 					elif data.loc[i,'play']=='no':
# 						setData2YesAndNo('rainy','cool','normal',False,'no')	

