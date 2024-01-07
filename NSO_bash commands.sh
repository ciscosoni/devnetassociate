# INSTALL DEPENDENCIES FOR UBUNTU 18.04
sudo apt update

sudo apt install python

sudo apt install default-jdk

sudo apt install xsltproc

sudo apt install make

sudo apt install ant

# DOWNLOAD it from Cisco Page (https://software.cisco.com/download/home/286331591/type/286283941/release/6.1) 
# AND EXTRACT NSO 
# UNPACK
sh nso-5.1.0.1.linux.x86_64.signed.bin
#INSTALL
sh nso-5.1.0.1.linux.x86_64.installer.bin $HOME/nso-6.1 --local-install

cd $home
# THIS NEXT COMMAND ALLOWS YOU TO USE NCS COMMANDS.
# DO NOT SKIP
source nso-6.1/ncsrc
# Make sure NCS knows which directory to run sims in. Create ncs-run if this errors
ncs-setup --dest $HOME/ncs-run
#Copy Cisco images and configs
cp -R nso-5.1/packages/neds/cisco-ios-cli-3.0 ncs-run/packages/cisco-ios-cli-3.0

cd ncs-run

ncs-netsim create-network $NCS_DIR/packages/neds/cisco-ios-cli-3.0 3 c

ncs-netsim start
# Enter the CLI for router c1
ncs-netsim cli-i c1

en

show run

exit
# Create the base configs for NSO based on the generated router configs
ncs-setup --netsim-dir ./netsim --dest .

ncs

ncs_cli -u admin

show configuration devices device
# Structured data!!
exit