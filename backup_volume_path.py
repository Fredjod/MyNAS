####
# Backup plan
# o: is for origine (source)
# d: is for destination
# Rsync origine / destination parameters
#### 
				
rsync_nodes = {
			"remote-to-local" : { 
				"bandwidth": 150, 
				"od" : [ 
					{ "o" : "-e \"ssh -i /home/user/.ssh/priv.key\" you@server.domain.com:/mnt/backup/FileHistory/MY-PC/",
					  "d" : "/mnt/Backup/FileHistory/MY-PC/"
					},
					{ "o" : "-e \"ssh -i /home/user/.ssh/priv.key\" you@server.domain.com:/mnt/backup/FileHistory/MY-PC2/",
					  "d" : "/mnt/Backup/FileHistory/MY-PC2/"
					}
				]
			},
			"local-to-remote" : { 
				"bandwidth": 600, 
				"od" : [ 
					{ "o" : "'/mnt/Backup/MY\ MAC.bundle/'",
					  "d" : "-e \"ssh -i /home/user/.ssh/priv.key\" 'you@server.domain.com:/mnt/backup/MY\ MAC.bundle/'"
					}
				]
			}
	}