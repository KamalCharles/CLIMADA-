import numpy as np
import scipy as sp
import matplotlib.pyplot as p

def lambda_mod_vm_rm(vmax,rmax,lat,r):
    f=2*7.2921e-5*np.sin(np.deg2rad(lat))
    lam=rmax/1.89
    b=r**2/(2*lam**2)
    a=(1/0.77)*(vmax+0.5*f*rmax)
    v=1.414*a*np.sqrt((1/b)*(1-np.exp(-b))-np.exp(-b))-0.5*f*r
    return v

#%%
def lambda_rth(vmax,rmax,lat,vth):
    if vmax<vth:
        rth=np.nan
    else:
        r=rmax
        while 1:
            v=lambda_mod_vm_rm(vmax,rmax,lat,r)
            if v<vth:
                rth=r
                break
            r=r+1000 
    return rth

#vmax=30
#rmax=80000
#lat=30
#r=np.arange(10,500)*1000.
#v=lambda_mod_vm_rm(vmax,rmax,lat,r)
#vth=18
#rth=lambda_rth(vmax,rmax,lat,vth)
#
#cmap = p.get_cmap("tab10")
#p.plot(r,v,'.')
#p.plot([rth,rth],[0,vth],color=cmap(1))
#p.plot([0,rth],[vth,vth],color=cmap(1))
#p.grid(1)
#p.xlim([0, 500000])
#p.ylim([0, vmax*1.05])



#%%
#def lambda_mod(r,a,lam,f):
#    alpha=(r**2)/(2*lam**2);
#    b=np.sqrt(alpha**-1*(1-np.exp(-alpha))-np.exp(-alpha));
#    c=0.5*f*r;
#    v=a*b-c;
#    return v
#
## solve lambda model for v=v
#def lambda_rv(rmax,vmax,f,v):
#
#    # clear
#    # rmax=50e3;
#    # vmax=60;
#    # f=2*7.2921e-5*np.sin(np.deg2rad(20));
#    
#    lam=rmax/1.89;
#    
#    #write the lambda model as V=a(P,rho)*b(lam,r)-c(f,r);
#    #a is r independant so calc using vmax,rmax
#    r=rmax;
#    alpha=(r**2.)/(2*lam**2);
#    b=np.sqrt(1/alpha*(1-np.exp(-alpha))-np.exp(-alpha));
#    c=0.5*f*r;
#    a=(vmax+c)/b;
#    
#    #   lam_fun=@(r) lambda_mod(a,r,lam,f)-v;
#    #  rv=fzero(lam_fun,[rmax rmax*100]);
#    def lambda_zero(r,a,lam,f,v):
#        v0=lambda_mod(r,a,lam,f)-v
#        return v0
#    
#    rv=sp.optimize.fsolve(lambda_zero,rmax,(a,lam,f,v))
#    
#    #plot(r,v); grid on
#    return rv[0]