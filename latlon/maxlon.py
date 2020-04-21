import numpy as np 
import scipy.io as sio



x=sio.loadmat('lonlatcdf_dat.mat',squeeze_me=True) 
loc_dat=x['lonlat_dat'] 

def gen_lonlat(dat): 
	cdf=dat['cdf'].item() 
	lon=dat['lon1d'].item()  
	xx=(cdf.nonzero())[0] 
	lonx=lon[xx]  
	return max(lonx)

print (gen_lonlat(loc_dat))
