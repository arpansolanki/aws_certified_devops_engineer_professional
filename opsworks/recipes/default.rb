#https://learn.chef.io/modules/learn-the-basics/ubuntu/bring-your-own-system/configure-a-package-and-service#/
apt_update 'Update the apt cache daily' do
  frequency 86_400
  action :periodic
end

package 'apache2'

service 'apache2' do
  supports status: true
  action [:enable, :start]
end

template '/var/www/html/index.html' do
  source 'index.html.erb'
end
