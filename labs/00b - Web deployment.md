# Web deployment

The deployment workflow will only use git and ssh. Make sure you are familiar with these tools. you can find some usefull resources online such as:
* https://guides.github.com/activities/hello-world/
* https://guides.github.com/introduction/git-handbook/

An interactive turorial can be found here https://asciinema.org/a/ayD7IbJhUgDKHAEe2lyCRJ9dM

1. Add your public key to dashboard.asterix.fei.tuke.sk
2. Create an application here dashboard.asterix.fei.tuke.sk
3. Once you have created your application on the dashboard. You will receive a link for your deployment in the form of `dokku@asterix.fei.tuke.sk:<unique-app-ip>`.
4. Add this remote to your current project
`git remote add asterix dokku@asterix.fei.tuke.sk:<unique-app-ip>`
5. Push your code to asterix.
`git push asterix master`
