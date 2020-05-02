#!/bin/bash

### PARAMS ###
VERSION=0.4

# Run unit testing
# Not Yet...

# Packaging
echo '--- Packaging... ---'
mkdir MyNAS
cp -r classes MyNAS/
rm -r classes/__pycache__
cp backup_volume_path.py MyNAS/
# cp backup.sh MyNAS/
cp BackupMain.py MyNAS/
chmod +x MyNAS/backup.sh
chmod +x MyNAS/BackupMain.py

if [ -e "MyNAS_$VERSION.tar.gz" ]
then
	rm MyNAS_$VERSION.tar.gz
fi
cd MyNAS
tar -zcf ../MyNAS_$VERSION.tar.gz ./*
echo '--- Package MyNAS_'$VERSION'.tar.gz is ready --- '
cd ..
rm -r ./MyNAS