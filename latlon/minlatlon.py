import numpy as np 
import scipy.io as sio



x=sio.loadmat('lonlatcdf_dat.mat',squeeze_me=True) 
loc_dat=x['lonlat_dat'] 

def gen_lonlat(dat): 
	cdf=dat['cdf'].item() 
	lon=dat['lon1d'].item() 
	lat=dat['lat1d'].item() 
	xx=(cdf>np.nonzero()[0][0] 
	lonx=lon[xx] 
	latx=lat[xx] 
	return [lonx,latx]

print (gen_lonlat(loc_dat))
