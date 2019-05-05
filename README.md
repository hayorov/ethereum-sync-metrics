# ethereum-sync-metrics
Python web3.py snippet that shows node sync statistics

## Quick start
   - Setup web3.py
   ```
   pip install -r requirements.txt
   ```
   
   - Define your node address in `metrics.py`
   ```
   web3 = Web3(Web3.HTTPProvider('https://xxxx.chainstack.com'))  # your node
   ```
   
  - Run `metrics.py`
  ```
  # python metrics.py
  2019-05-06 01:00:32 avg: 1827 max: 1938 min: 1378 states/s 	remain: 136604075 states	 4 peers 	eta@ 20:46:28.165828
  2019-05-06 01:00:37 avg: 1864 max: 1938 min: 1378 states/s 	remain: 136595500 states	 3 peers 	eta@ 20:21:14.951050
  2019-05-06 01:00:42 avg: 1791 max: 1938 min: 1378 states/s 	remain: 136583359 states	 3 peers 	eta@ 21:11:16.481006
  2019-05-06 01:00:48 avg: 1742 max: 1938 min: 1378 states/s 	remain: 136580287 states	 3 peers 	eta@ 21:46:35.797305
  2019-05-06 01:00:53 avg: 1721 max: 1938 min: 1378 states/s 	remain: 136575694 states	 3 peers 	eta@ 22:03:01.154434
  2019-05-06 01:00:58 avg: 1682 max: 1938 min: 1378 states/s 	remain: 136569043 states	 4 peers 	eta@ 22:33:15.402442
  2019-05-06 01:01:03 avg: 1698 max: 1938 min: 1378 states/s 	remain: 136564293 states	 3 peers 	eta@ 22:20:27.458747
  ```
