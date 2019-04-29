# Build Instructions for Mondified Bind

sudo passwd root
su
apt-get update
apt-get upgrade
apt-get install gcc,postgresql,unzip,make,libpq-dev,libtool

# Copy repo up to current directory
cp Netsec-project-master.zip ./bind/netsec.zip
cd bind
cd Netsec-project-master/
chmod +x ./configure
mv config.cache config.cache.old

./configure --build 'i686-pc-linux-gnu' --host 'i686-pc-linux-gnu' --target 'mingw' --with-dlz-postgres=/usr/lib/postgresql/
make
make install
service named start
touch /etc/named.conf
vim /etc/named.conf
# Modify conf
service named stop
service named start