# Remote-Desktop-Caching-
This tool allows one to recover old RDP (mstsc) session information in the form of broken PNG files. These PNG files allows Red Team member to extract juicy information such as LAPS passwords or any sensitive information on the screen. Blue Team member can reconstruct PNG files to see what an attacker did on a compromised host. It is extremely useful for a forensics team to extract timestamps after an attack on a host to collect evidences and perform further analysis.

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)

# Screenshots
On the first run of the `Remote-Desktop-Caching` using `python.exe remotecache.py` user will get options as below:
![image](https://user-images.githubusercontent.com/3501170/43398352-2e55ef68-944b-11e8-8467-60ab35a38095.png)

Using `Option 1` and `Option 2` user can know the current session execution policy and set it to `Bypass` which executes the `rdpcache.ps1` PowerShell script. USing `Option 3` user can list the cached binary files which is going to be used to reconstruct PNG files.

![image](https://user-images.githubusercontent.com/3501170/43397595-bada2b14-9448-11e8-8eba-2bc3d0efd853.png)

Choosing `Option 4`: Starts analyzing cache files and reconstruction process. This option creates a folder in user C drive with a name of `Recovered_RDP_Sessions`

![image](https://user-images.githubusercontent.com/3501170/43398692-2c76f718-944c-11e8-8b77-0ed263967e08.png)

Sensitive information is recovered from these binary files in the form of broken PNG images. Managed to recover `LAPS password`, `Attacker IP address` and `malicious file names`. It also reveals some of the crucial information about attacker activities on a compromised host. For forensics team `timestamp` is revealed in most of these recovered images. 

![image](https://user-images.githubusercontent.com/3501170/43517110-ec957090-95ca-11e8-9d2b-d55fe07fdecf.png)

# How do I use this?
<pre>
- git clone https://github.com/Viralmaniar/Remote-Desktop-Caching-.git
- python.exe remotecache.py
</pre>

# Questions?

Twitter: https://twitter.com/maniarviral <br>
LinkedIn: https://au.linkedin.com/in/viralmaniar

# Contribution & License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</br>
Want to contribute? Please fork it and hit up with a pull request.

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)
