from matplotlib import pyplot as plt

x=[1,2,5,7]
y=[2,8,10,3]
fig_data={
'title':["original figure","Median-Absolute-Slope \n Banking","Average-Absolute-Orientation \n Banking","Weighted Average-Absolute-Orientation \n Banking"],
'aspect_ratio':[0.5,8/21,0.434654,0.7667693]
}

f,plots=plt.subplots(1,4)

for i,p in enumerate(plots):
    p.axes.set_aspect(aspect=fig_data['aspect_ratio'][i])
    if i==0: p.set_ylabel('y')
    p.set_xlabel('x')
    p.set_title(fig_data['title'][i])
    p.plot(x,y)

plt.show()

