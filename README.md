# mTLS
Web app sends data like new student record and retrieves data too on request from mongo. Put cert-manager with envoy proxy to make sure all the data is flowing via mTLS and certificate is issued every one hour and pods are able to retrieve latest certificate to ensure mTLS traffic between pods
