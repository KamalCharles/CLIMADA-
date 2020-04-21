import scipy.io as sio
import event_gen_funcs as eg
from geopy import distance

def event_selector(events,lon,lat):
    eth=[]
    # calc dist between lat,lon and landfall event
    dist=[distance.distance((e['lat'],e['lon']),(lat,lon)).m for e in events]
    #get radius rx to wind speed thresh vx
    rx=[e['rx'] for e in events]
    #filter for events above vx at lat,lon
    for e in range(len(events)):
        if dist[e]<rx[e]:
            eth.append(events[e])
    return eth

def event_generator(nY,vx,Z500a):
    # load Z500 parametrization data and use to get number of events for 1 year
    x=sio.loadmat('param_dat.mat',squeeze_me=True)
    nEv_dat=x['param_dat']
    
    # load location param data
    x=sio.loadmat('lonlatcdf_dat.mat',squeeze_me=True)
    loc_dat=x['lonlat_dat']
    
    # load pressure gen dat
    x=sio.loadmat('pdeffit_dat.mat',squeeze_me=True)
    pdef_dat=x['logpdef_dat']
    
    # load pressure gen dat
    x=sio.loadmat('vmax_dat.mat',squeeze_me=True)
    vmax_dat=x['vmax_dat']
    
    # load rain gen dat
    x=sio.loadmat('rain_dat.mat',squeeze_me=True)
    rain_dat=x['rain_dat']
    
    # model inputs
    #Z500a=+0  # Z500 anomaly parameter
    #vx=18  # wind intensity threshold
    #nY=68  # no. years
    
    evs=[]
    for y in range(nY):
        nEv=eg.gen_nEvs(nEv_dat,Z500a)
        for i in range(nEv):
            loc=eg.gen_lonlat(loc_dat)
            lon=loc[0]
            lat=loc[1]
            pdef=eg.gen_pdef(pdef_dat,lat)
            vmax=eg.gen_vmax(vmax_dat,pdef,lat);
            rmax=eg.gen_rmax(vmax, lat)
            rx=eg.gen_rx(rmax,vmax,lat,vx)
            Pvol=eg.gen_rain(rain_dat,rmax,vmax,lat)
            ev={'year':y,'lon':lon,'lat':lat,'pdef':pdef,'vmax':vmax,'rmax':rmax,'rx':rx,'Pvol':Pvol};
            evs.append(ev)
            
    return evs 
    #vs=[i['pdef'] for i in evs]    
    #rxs=[i['rx'] for i in evs if np.isfinite(i['rx']) ]
    
    #loc = np.asarray(loc) 
    #plt.plot(loc[:,0], loc[:,1],'.k')
    #plt.show()
    #plt.hist(vs)
    
    #print(len(evs))
