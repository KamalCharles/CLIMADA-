import numpy as np 
import scipy.io as sio



x=sio.loadmat('lonlatcdf_dat.mat',squeeze_me=True) 
loc_dat=x['lonlat_dat'] 

def gen_maxlon(dat): 
	cdf=dat['cdf'].item() 
	lon=dat['lon1d'].item()  
	xx=(cdf.nonzero())[0] 
	lonx=lon[xx]  
	return max(lonx)
print('Maximum longitude')
print (gen_maxlon(loc_dat))


def gen_minlon(dat):
	cdf=dat['cdf'].item() 
	lon=dat['lon1d'].item()  
	xx=(cdf.nonzero())[0] 
	lonx=lon[xx]  
	return min(lonx)
print('Minimum longitude')
print (gen_minlon(loc_dat))


def gen_maxlat(dat): 
	cdf=dat['cdf'].item() 
	lat=dat['lat1d'].item()  
	xx=(cdf.nonzero())[0] 
	latx=lat[xx]  
	return max(latx)
print('Maximum latitude')
print (gen_maxlat(loc_dat))


def gen_minlat(dat): 
	cdf=dat['cdf'].item() 
	lat=dat['lat1d'].item()  
	xx=(cdf.nonzero())[0] 
	latx=lat[xx]  
	return min(latx)
print('Minimum latitude')
print (gen_minlat(loc_dat))




