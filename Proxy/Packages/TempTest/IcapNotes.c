  388         /* Check client Ip against SquidClamav trustclient */
  389         if ((clientip = ci_headers_value(req->request_header, "X-Client-IP")) != NULL) {
  390         debugs(2, "DEBUG X-Client-IP: %s\n", clientip);
  391         ip = inet_addr(clientip);
  392         chkipdone = 0;
  393         if (dnslookup == 1) {
  394             if ( (clientname = gethostbyaddr((char *)&ip, sizeof(ip), AF_INET)) != NULL) {
  395             if (clientname->h_name != NULL) {
  396                     if (scan_mode == SCAN_ALL) {
  397                     /* if a TRUSTCLIENT match => no virus scan */
  398                     if (client_pattern_compare(clientip, clientname->h_name) > 0) {
  399                     debugs(2, "DEBUG no antivir check (TRUSTCLIENT match) for client: %s(%s)\n", clientname->h_name, clientip);
  400                     return CI_MOD_ALLOW204;
  401                     }
  402                 } else {
  403                     /* if a UNTRUSTCLIENT match => virus scan */
  404                     if (client_pattern_compare(clientip, clientname->h_name) > 0) {
  405                     debugs(2, "DEBUG antivir check (UNTRUSTCLIENT match) for client: %s(%s)\n", clientname->h_name, clientip);
  406                         scanit = 1;
  407                     }
  408                 }
  409                 chkipdone = 1;
  410             }
  411             }
  412         }
