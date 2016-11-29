# MyNAS

## Motivations
The motivations came from few key observations:
  - People ofen uses external USB drive for backing up their PC/Mac data (documents, photos, videos) and for storing some archives (freeing space on their laptop).
  - On their external backup disk (500 GB to 1 TB), there is often pleinty of free space
  - Those personal data are not really secured, because the PC/Mac and its backup are located on the same place/house. In addition, there is no backup of their archive.
  - The cloud storage plans look good as a solution, however, for an 1TB space, the plan costs 120 euros/year (in 2016), without taking account the ecological footprint of the underlying datacenters. As a comparaison, a 1TB USB external drive costs around 60 euros.

## Idea
Why should we connect over the internet the free spaces that we already all have on our backup disks? This should permit, without any recurrent costly cloud plan to:
  - Have a remoted copy of our data, and make them secured.
  - Have a backup of our archives.
  
**The solution:**
  - Plug our external USB drive behind a raspberry-pi at home. Since the v3 (early 2016), the raspberry-pi USB ports can power an external drive.
  - At home, use the Internet box as a router for using the raspberry-pi + USB disk like a NAS over the home LAN. The PC/MAC are backed up by mounting a network drive and use the backup software provided by Microsoft (File History) and Apple (Timemachine).
  - Inter-connect over the Internet several raspberry-pi + USB disk in a secure way (SSL w/ RSA key), for creating a network of storage nodes.
  - Add a layer of software for managing the network of stortage nodes:
    - Declare node / and available freespace (quota)
    - Setup the synchronisation of data/directories between nodes
    - Monitor the synchronisation, space usage, etc...
This is the purpose of the code in this Github repository.
