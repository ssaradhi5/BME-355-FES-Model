import numpy as np
import matplotlib.pyplot as plt

offset_time=10
offset_time=int(offset_time/2)
slope=0.1
max_value=1
step_size=1
time_tomax=max_value/slope




slope_inc=0
slope_dec=0
counter=0
offset_time_adjusted=offset_time/step_size




# for i,value in enumerate(times):

#   if slope_inc<max_value:
#     output[i]=slope_inc
#     slope_inc=slope_inc+(slope*0.1)
#     counter+=1
  

#   if slope_inc==max_value:
#     output[i+offset_time_adjusted]=max_value
#     break


time_tomax=int(time_tomax/step_size)
offset_time=int(offset_time/step_size)

times=np.arange(0,offset_time_adjusted+(time_tomax*2)+step_size,step_size)
output=np.zeros((times.shape))

# print(time_tomax)

slope_array=np.arange(0,max_value,slope*step_size)
decrease_slope=np.arange(max_value,0,-slope*step_size)
print(slope_array)


output[0:time_tomax]=slope_array

output[time_tomax: (offset_time + time_tomax)]= max_value

output[offset_time + time_tomax : -1]=decrease_slope

plt.plot(output)
plt.show()