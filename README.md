# MyNAS

## Observations and Motivations

  - People ofen uses external USB drive for backing up their PC/Mac data (documents, photos, videos) and for storing some archives (freeing space on their laptop).
  - On their external backup disk (500 GB to 1 TB), there is often pleinty of free space
  - Those personal data are not really secured, because the PC/Mac and its backup are located on the same place/house. In addition, there is no backup of their archive.
  - A cloud storage plan is sold as a solution to this need, however for an 1TB space, the plan costs 120 euros/year (in 2016), without taking into account the ecological cost of the underlying mega datacenters (Amazon, Apple, Microsoft, etc...). As a comparaison, a 1TB USB external drive costs around 60 euros and use 50 cm2 of your living room...
  - More and more people are connected to the Internet with the fibre, allowing high speed inter-connexion between private individual locations.

**Idea:**
Why should we connect over the internet the free spaces that we already all have on our backup disks? This should permit, without any recurrent costly cloud plan to:
  - Have a remoted copy of our data, and make them secured.
  - Have a backup of our archives.
  
## Solution
  - Plug our external USB drive behind a raspberry-pi at home. Since the v3 (early 2016), the raspberry-pi USB ports can power an external drive. Raspberry-pi v3 costs 56 Euros TTC. Any USB disk (already used for manual backup) can be plugged to the raspberry USB port. 
  - At home, use of the Internet box as a router for using the raspberry-pi + USB disk like a NAS. The PC/MAC are backed up by mounting a network drive and use the backup software provided by Microsoft (File History) and Apple (Timemachine).
  - Inter-connect over the Internet several family/friends raspberry-pi + USB disk in a secure way (SSL w/ RSA key), for creating a network of storage nodes.
  - The File History, Timemachine and other archive data are replicated in a daily basis over this network of storage nodes, making those fully secured... Even if a day your house was on fire (I don't wish you this), your life videos/photos would be safed on a disk of a friend or familly member!
  - Add a layer of code (bash, python, Django?, HTML5?) for managing the network of stortage nodes in a graphical fashion:
    - Declare node / and available freespace (quota)
    - Setup the synchronisation of data/directories between nodes
    - Monitor the synchronisation, disk usage, etc...
    
This is the purpose of the code in this Github repository.
