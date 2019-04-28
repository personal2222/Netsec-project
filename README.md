  
  
The proxy code is located in the Webby directory
* download/install [nvm](https://github.com/creationix/nvm)
* use nvm to install latest version of node `nvm install node`
* install dependencies with `npm install`
* enable https for webserver by creating key (skynet.com.key) and cert (skynet.com.crt) with openssl
* launch web server from project directory with `npm start`
* launch proxy server from project directory with `node server/proxy.js`
* use firefox browser and manually set proxy configuration to localhost:8080 for all protocols
* run URL_Classify.py in the Classifier2 directory. Make sure the require python packages below are installed.
* visit the interweb

Classification analysis
Classifier2/classifier notebook.ipynb contains code for the analysis we performed on the classifier. Make sure the other files in Classifier2 are in the same directory when you try to run it.  
  
Required Python packages:  
requests  
Flask  
whois    
tldextract  
joblib  
numpy  
scikit_learn==0.19.1  
scipy  

