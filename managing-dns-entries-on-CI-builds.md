#### Managing DNS entries on CI builds

**Problem Statement**

> Continuous integration process creates intermediate build(s) against each branch and if we need to test a certain branch a seperate URL is needed for better management as compared to hosting branches with different IP address or port number.

**Constraints**

* Bitbucket to be used as git repo
* Amazon EC2 Intances to be used as servers for DNS and Developement webserver.
* Developement server i.e. will host the branch specific web application(s).
* All servers will use `ubuntu 18.04` OS.
* Webserver will use `ngnix` with `php-fpm`

**Recommended Solution**

* Internal DNS server needs to be provisioned for resolving branch specific URLs to developement web server's IP address.
* `bind9` will be used for DNS server software. 
* three nameserver Instances i.e. ns1(primary), ns2(secondary) and ns3(secondary) to be used and configured.
* Wildcard forward Lookup DNS entry will be created to resolve branch specific subdomains (a working config snippet below)
```
*.vikilabs.local.             IN      A      10.10.10.60
```
here `branch01.vikilabs.local` or `branch02.vikilabs.local` will resolve to same server `10.10.10.60`
* Ngnix vhost configuration will re-route the request to branch specific sites (a working config snippet below)
```
server {
  listen :80;

  server_name ~^(.+).vikilabs.local$;

  if ($host ~ "^(.+).vikilabs.local$") {
    set $site $1;
  }

  root /var/www/$site;
  #more stuff
}
```
