from dotenv import load_dotenv
import os
from constants import (START_BLOCK, 
                       BALANCER_VAULT_CONTRACT, 
                       COW_AMM_MAINNET_ADDRESS, 
                       ORIGINAL_BLOCK, 
                       BALANCER_SWAP_TOPIC)
i=0

load_dotenv()
API_KEY = os.getenv("GNOSISSCAN_KEY")

url = (
            "https://api.gnosisscan.io/api?module=logs&action=getLogs&address="
            + BALANCER_VAULT_CONTRACT
            + "&topic0="
            + BALANCER_SWAP_TOPIC
            + "&and&topic_1=0XB8BB1CE9C6E5401D66FE2126DB6E7387E1E24FFE000200000000000000000181"
            + "&fromBlock="
            + str(START_BLOCK)
            + "&toBlock=32236669&page="
            + str(i)
            + "&offset=1000&apikey="
            + API_KEY
        )

print(url)
print("0xB8bB1ce9C6E5401D66fE2126dB6E7387E1E24fFE".upper())

#0xDE8C195AA41C11A0C4787372DEFBBDDAA31306D2000200000000000000000181
#0XB8BB1CE9C6E5401D66FE2126DB6E7387E1E24FFE -> get it from the url of the balancer pool
#0xb8bb1ce9c6e5401d66fe2126db6e7387e1e24ffe00020000000000000000003d
# from https://app.balancer.fi/#/gnosis-chain/pool/0xb8bb1ce9c6e5401d66fe2126db6e7387e1e24ffe00020000000000000000003d
# or via gnosisscan -> logs -> swap event -> topic

# 0xBA12222222228d8Ba445958a75a0704d566BF2C8
#small change