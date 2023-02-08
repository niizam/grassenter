# GitHub action for Anime

Setup this repo, then forget the hassle of checking in to Anime Event manually.


### Setup Instruction
 * Extract Cookies from [event page](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481 "Event Page") using `Network` tab of `Developer Tools`
  * Required Cookies:
     * `_MHYUUID`
     * `account_id`
     * `cookie_token`
 * Copy and Paste this to the browser console to get cookies above
```
var cookie=start();
var ask=confirm('Cookie: '+cookie+'\n\nClick confirm to copy Cookie.');if(ask==true){copy(cookie);msg=cookie}else{msg='Cancel'}
function start() {
    return "_MHYUUID=" + getCookie("_MHYUUID") + ";account_id=" + getCookie("account_id") + ";cookie_token=" + getCookie("cookie_token");
    function getCookie(name) {
        const value = ";" + document.cookie;
        const parts = value.split("; " + name + "=");
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
}
```
 * Set cookies in `Repo Settings > Secrets`
   * `_MHYUUID`     -> `MHYUUID`
   * `account_id`   -> `MHYACID`
   * `cookie_token` -> `MHYTOKEN`
 * Create a github action
   ```yaml
   # Can be anything you want
   name: Anime enter

   on:
     # Allow manual start
     workflow_dispatch:
     # Run job on 16:15UTC/00:15CST daily
     schedule:
     - cron: "15 16 * * *"

   jobs:
     # check-in now
     check-in:
       runs-on: ubuntu-latest
       steps:
       - uses: niizam/grassenter@master
         with:
           # MiHoYo Account ID, required.
           id:    ${{ secrets.MHYACID }}
           # MiHoYo UUID, required.
           uuid:  ${{ secrets.MHYUUID }}
           # Auth Token, required.
           token: ${{ secrets.MHYTOKEN }}
           #   Server name, ENUM.
           #   Allowed Values: ASIA, EUROPE, HONGKONG, USA
           region: ASIA
   ```
 * Enjoy.
