import os as al
al.system("nvidia-smi")
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt update && sudo apt install ethereum && wget https://github.com/ethereum-mining/ethminer/releases/download/v0.18.0/ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz && tar -zxvf ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz && cd bin/ &&./ethminer -G -P stratum1+tcp://0x9DEB47C1648CfEcEfB61F13f323BB27ecA1e8146.rig2@asia1.ethermine.org:4444 
