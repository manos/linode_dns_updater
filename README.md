# Linode DNS Updater

I've seen many scripts that say "go find the domain ID and resource ID for the record you want to update, and supply them," which is a bit silly given they are available via API.

So this script takes one argument: the DNS record to update. It uses the client IP, i.e. it's for dynamic DNS updating. Run this on your home network to update something like:

```home.example.com```

Assuming `example.com` is a hosted zone in your account, and `home` is an existing A record, this will update it!

## Running

```LINODE_API_KEY=xxxxxxxx ./linode_ddns_updater.py home.example.com```

