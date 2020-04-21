import event_gen
import csv

#output file
fout='events.csv'

# model inputs
Z500a=+0  # Z500 anomaly parameter
vx= int(input('Enter wind intensity threshold: '))  # wind intensity threshold
nY= int(input('Enter number of years: '))  # no. years

# Hong Kong


x = None
y = None

print ('Select location')
print ('1. Hong Kong - x=114.149; y=22.286')
print ('2. Shanghai  - x=121.522; y=31.267')

choice = input('Select 1 or 2: ')
if choice == '1':
    x = 114.149
    y = 22.286
elif choice == '2':
    x = 121.522
    y = 31.267
else:
    print('Invalid input')

# Shanghai
#x=121.522;y=31.267;

#gen China events
events=event_gen.event_generator(nY,vx,Z500a)
#select local threshold exceeding events
eth=event_gen.event_selector(events,x,y)

#convert to km
for e in eth:
    e['rmax']=e['rmax']/1000
    e['rx']=e['rx']/1000


#%% write to csv
headings={'year':'event_id', 'lon':'lon', 'lat':'lat', 'pdef':'Delta pressure (hPa)', 'vmax':'Vmax (m/s)', 'rmax':'Rmax (km)', 'rx':'Rthresh (km)', 'Pvol':'Pvol (m^3/hr within 500km)'}  
toCSV=eth
with open(fout, 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, 
                        fieldnames=toCSV[0].keys(),
                        )
    #fc.writeheader()
    fc.writerow(headings)
    fc.writerows(toCSV)

def climada_events(): 
    headings={'year':'event_id', 'lon':'lon', 'lat':'lat', 'pdef':'Delta pressure (hPa)', 'vmax':'Vmax (m/s)', 'rmax':'Rmax (km)', 'rx':'Rthresh (km)', 'Pvol':'Pvol (m^3/hr within 500km)'}
toCSV=eth
with open(fout, 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file,
                        fieldnames=toCSV[0].keys(),
                        )
    #fc.writeheader()
    fc.writerow(headings)
    fc.writerows(toCSV)

if __name__ == "climada_events":
    main()

