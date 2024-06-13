import statistics
import pandas as pd
import random
import plotly.figure_factory as ff 
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")

df.head()

gender=df['gender'].tolist()
race=df['race/ethnicity'].tolist()
parental=df['parental level of education'].tolist()
lunch=df["lunch"].tolist()
course=df['test preparation course'].tolist()
mscore=df["math score"].tolist()
rscore=df["reading score"].tolist()
wscore=df["writing score"].tolist()


# for maths score

mean=statistics.mean(mscore)
median=statistics.median(mscore)
mode=statistics.mode(mscore)
sd=statistics.stdev(mscore)
print(f'Mean:{mean}')
print(f'Median:{median}')
print(f'Mode:{mode}')
print(f'Standard Deviation:{sd}')

# for reading score

mean1=statistics.mean(rscore)
median1=statistics.median(rscore)
mode1=statistics.mode(rscore)
sd1=statistics.stdev(rscore)
print(f'Mean:{mean1}')
print(f'Median:{median1}')
print(f'Standard Deviation:{sd1}')

#for writing score

mean2=statistics.mean(wscore)
median2=statistics.median(wscore)
mode2=statistics.mode(wscore)
sd2=statistics.stdev(wscore)
print(f'Mean:{mean2}')
print(f'Median:{median2}')
print(f'Mode:{mode2}')
print(f'Standard Deviation:{sd2}')




# sd for wscore

first_stdev_start,first_stdev_end= mean-sd,mean+sd
second_stdev_start,second_stdev_end= mean-2*sd,mean+2*sd
third_stdev_start,third_stdev_end= mean-3*sd,mean+3*sd

data1=[result for result in mscore if result>first_stdev_start and result<first_stdev_end]
n1=len(data1)


data1=[result for result in mscore if result>first_stdev_start and result<first_stdev_end]
n11=len(data1)


data1=[result for result in mscore if result>first_stdev_start and result<first_stdev_end]
n11=len(data1)

fig=ff.create_distplot([mscore],['Maths results'],show_hist=False)
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.15],name='First Standard Deviation Start'))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.15],name='First Standard Deviation End'))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.15],name='Second Standard Deviation Start'))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.15],name='Second Standard Deviation End'))
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.15],name='Third Standard Deviation Start'))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.15],name='Third Standard Deviation End'))
fig.show()


# sd for rscore

first1_stdev_start,first1_stdev_end= mean1-sd1,mean1+sd1
second1_stedv_start,second1_stdev_end= mean1-2*sd1,mean1+2*sd1
third1_stdev_start,third1_stdev_end= mean1-3*sd1,mean1+3*sd1

data2=[result for result in rscore if result>first1_stdev_start and result<first1_stdev_end]
n2=len(data1)


data21=[result for result in rscore if result>second1_stedv_start and result<second1_stdev_end]
n21=len(data21)


data22=[result for result in rscore if result>third1_stdev_start and result<third1_stdev_end]
n22=len(data22)

fig1=ff.create_distplot([rscore],['Reading score'],show_hist=False)
fig1.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.15],name='First Standard Deviation Start'))
fig1.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.15],name='First Standard Deviation End'))
fig1.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.15],name='Second Standard Deviation Start'))
fig1.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.15],name='Second Standard Deviation End'))
fig1.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.15],name='Third Standard Deviation Start'))
fig1.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.15],name='Third Standard Deviation End'))
fig1.show()


# sd for wscore

first2_stdev_start,first2_stdev_end= mean2-sd2,mean2+sd2
second2_stedv_start,second2_stdev_end= mean2-2*sd2,mean2+2*sd2
third2_stdev_start,third2_stdev_end= mean2-3*sd2,mean2+3*sd2

data3=[result for result in wscore if result>first2_stdev_start and result<first2_stdev_end]
n3=len(data1)


data31=[result for result in wscore if result>second2_stedv_start and result<second2_stdev_end]
n31=len(data31)


data32=[result for result in wscore if result>third2_stdev_start and result<third2_stdev_end]
n32=len(data32)

fig2=ff.create_distplot([wscore],['Writing score'],show_hist=False)
fig2.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.15],name='First Standard Deviation Start'))
fig2.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.15],name='First Standard Deviation End'))
fig2.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.15],name='Second Standard Deviation Start'))
fig2.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.15],name='Second Standard Deviation End'))
fig2.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.15],name='Third Standard Deviation Start'))
fig2.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.15],name='Third Standard Deviation End'))
fig2.show()





