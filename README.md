# Remote-Desktop-Caching-
This tool allows one to recover old RDP (mstsc) session information in the form of broken PNG files. These PNG files allows Red Team member to extract juicy information such as LAPS passwords or any sensitive information on the screen. Blue Team member can reconstruct PNG files to see what an attacker did on a compromised host. It is extremely useful for a forensics team to extract timestamps after an attack on a host to collect evidences and perform further analysis.

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)

# Screenshot
On the first run of the `Remote-Desktop-Caching` using `python.exe remotecache.py` user will get options as below:
![image](https://user-images.githubusercontent.com/3501170/43398352-2e55ef68-944b-11e8-8467-60ab35a38095.png)

Using `Option 1` and `Option 2` user can know the current session execution policy and set it to `Bypass` which executes the `rdpcache.ps1` PowerShell script

![image](https://user-images.githubusercontent.com/3501170/43397595-bada2b14-9448-11e8-8eba-2bc3d0efd853.png)
