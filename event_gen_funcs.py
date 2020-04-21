import numpy as np
import lambda_mod_funcs as lmf

def gen_nEvs(dat,param):
    annualfreq=dat['c'] + param*dat['m']
    nEv=np.random.poisson(annualfreq)
    return nEv

def gen_lonlat(dat):
    cdf=dat['cdf'].item()
    lon=dat['lon1d'].item()
    lat=dat['lat1d'].item()
    xx=(cdf>np.random.rand()).nonzero()[0][0]
    
    lonx=lon[xx]    
    latx=lat[xx]
    return [lonx,latx]

def gen_pdef(dat,lat):
    mu=dat['mu_c']+dat['mu_m']*lat;
    sig=dat['sig_c']+dat['sig_m']*lat;
    logpdef=mu+sig*np.random.randn();
    pdef=np.exp(logpdef);
    return pdef

def gen_vmax(dat,pdef,lat):
    vmax=dat['a']*np.log(pdef)+dat['b']*lat+dat['c']+np.random.randn()*dat['rmse'];
    if vmax < 0:
        vmax=0
    return vmax

def gen_rmax(vmax,lat):
    #RmaxKZ
    rmax=(66785-176.92*vmax+1061.9*(lat-25));
    return rmax

def gen_rx(rmax,vmax,lat,vx):
    return lmf.lambda_rth(vmax,rmax,lat,vx)

def gen_rain(dat,rmax,vmax,lat):
    # get rain using lambda for R18
    if vmax>18:
        r18=lmf.lambda_rth(vmax,rmax,lat,18)
    else:
        r18=rmax;
    #rain=vmax*dat.a+r18./1000*dat.b+dat.c+dat.rmse*randn;
    rain=vmax*dat['a']+r18/1000*dat['b']+dat['c']
    if rain<0:
        rain=0
    return rain

