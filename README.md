# MyNAS

## Motivations
The motivations came from few constations:
  - People ofen use external USB drive for backing up their PC/Mac data (documents, photos, videos) and stored some archives for freeing space on their laptop.
  - On this backup disk, there are often pleinty of free space
  - Those data are not really secured, because the PC/Mac and its backup are located on the same place/house and there is no backup of the archives
  - The cloud storage plan looks good, but for an 1TB space (80 euros disk), the plan costs 120 euros/year (in 2016), without taking account the ecology footprint of the underlying datacenter.
  
Why should we tried to connect over the internet the free space that we already all have on our backup disk?
  - Have a remoted copy of our data
  - Have a backup of our archive
  
**The solution**:
  - Plug our external USB drive behind raspberry-pi at home.
  - At home, use the Internet box as a router for using the raspberry+usb disk like a NAS over the home LAN.
  - Inter-connect over the Internet several raspberry-pi+usb disk in a secure way, for creating a network of storage nodes (and availabke free space)
  - And monitor automatic process, free spaces, etc... for synchroning data between each node.
