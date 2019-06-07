# notes-to-self

----------------------------
## KamKaz

#### System Security
https://blog.ssdnodes.com/blog/secure-ansible-playbook-2/  


#### Random shell commands
```
#Look for string in all files
fgrep -e"PublicationStatus" *.xml 
```
#### K8s
https://kubernetes.io/blog/2019/03/15/kubernetes-setup-using-ansible-and-vagrant/  
https://www.vikki.in/kubernetes-on-ubuntu-18-04-with-dashbaoard/

#### MySql
https://severalnines.com/resources/tutorials/mysql-replication-high-availability-tutorial  
https://planet.mysql.com/entry/?id=5988531  

#### Terraform
https://pragmacoders.com/blog/creating-an-ec2-instance-with-terraform  

##### CI/CD AzureDevOps
https://www.adcisolutions.com/knowledge/continuous-integration-drupal-8-and-gitlab-cicd  
https://www.valentinog.com/blog/drupal-ci/  

#### Artifacts
https://www.azuredevopslabs.com/labs/vstsextend/ansible/ 

#### Azure DevOps Extension
https://marketplace.visualstudio.com/items?itemName=qetza.replacetokens&targetId=915e07e1-c4e8-4f2c-95f0-d84b8c6e497a

#### Deployment via release pipeline
```
# Extract tarball from build
cd /home/ubuntu/build-releases/
tar -zxvf 20190426.1.tar.gz --one-top-level
cd /var/www/
# --- drush maintenance mode -- On --- # 
cd /var/www/html
# db backup
vendor/bin/drush sql:dump --result-file=/vagrant/backups/286.sql
# Code Backup
sudo mv /var/www/html/ /home/vagrant/build-releases/release-$(date +'%Y%m%d-%H%M')
# Remove symlink if exist
sudo rm html
# symlink pointing to new release
sudo ln -s /home/vagrant/build-releases/277/ /var/www/html
# --- drush maintenance mode -- Off --- #


##### Tips
([ -h html ] && echo sym exists) || ([ -d html ] && echo dir exists)
```

#### nginx | webserver, reverse-proxy, loadbalancer
* as a loadbalencer :  
https://www.youtube.com/watch?v=v81CzSeiQjo  

* as a reverse proxy for apache  
https://www.youtube.com/watch?v=qPiQXG4JrHc

----------------------------------
https://www.geeksareforlife.com/blog/2018/05/13/vagrant-and-nfs  
http://docs.drupalvm.com/en/latest/other/performance/  
https://hollyit.net/blog/windowsvagrantwinnfsd-without-file-update-problems  
https://github.com/Microsoft/windows-dev-box-setup-scripts/blob/master/scripts/WSL.ps1  

##### set-up-dev-tasks

![image](https://user-images.githubusercontent.com/13016162/53466243-3cf94880-3a77-11e9-9c73-134aa04928bf.png)

![image](https://user-images.githubusercontent.com/13016162/53471541-07f6f100-3a8b-11e9-936d-6414ae7059bf.png)


  Test Case      |                                    Result                                                                   |
  ---                |                                                                        ---                                     |
Without NFS  | 60 Milliseconds - 70 Milliseconds (web resp from home page load)     |
With NFS        | 30 Milliseconds - 40 Milliseconds (web resp from home page load)    |

* Solr and New Relic
https://docs.newrelic.com/docs/insights/insights-api/get-data/query-insights-event-data-api

* SSL Ceritificates

https://www.entrust.com/wp-content/uploads/2014/11/Six-Steps-SSL-Management-WEB-Nov15.pdf
https://community.digicert.com/en/blogs.entry.html/2014/08/11/types-of-ssl-certificateschoose-the-right-one.html

### pdf convert API
```
https://url-to-pdf-api.herokuapp.com/api/render?url=http://hclpandv.github.io/online-cv/&pdf.format=a4&pdf.landscape=true&pdf.pageRanges=1-2&pdf.margin.top=0.5cm
```

### QA Integration
https://humanwhocodes.com/blog/2015/10/triggering-jenkins-builds-by-url/


#### postfix on ubuntu
https://www.youtube.com/watch?v=yHUigLSmGOE  
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/postfix.html  

---------------------------
## GharBar

https://www.livspace.com/custom-modular-kitchens

https://www.marksdzyn.com/  
https://www.planmyinterior.com/  
https://hometriangle.com/   
http://www.mgmkitchens.in/modular-kitchen-ideas/  

http://am2pmmodularkitchens.com/  
http://www.regalokitchens.com/  
http://www.myfurnituremyway.com/modular-kitchens-online

* painting

~~https://paintmywalls.in/painters-in-delhi/.~~ DO NOT WORK IN DELHI NCR  
https://broomberg.in/painting-service  
http://www.apwncw.com/
http://easypainter.in/reviews.html

http://www.shabadinteriors.com/our-services.php

* for flooring and window blinds
http://www.interiorsolutions.co/contact-us.html

