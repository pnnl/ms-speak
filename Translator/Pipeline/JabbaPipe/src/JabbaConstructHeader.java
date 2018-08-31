


public class JabbaConstructHeader {


    // makes the HTTP header for the response
    // the headers job is to tell the caller the result of the request
    public final static String construct_http_header(int return_code, int file_type, int length) {
        /*
         * 200's are used for successful requests. 300's are for redirections. 400's
         * are used if there was a problem with the request. 500's are used if there
         * was a problem with the server.
         */
        String s = "HTTP/1.1 ";
        switch (return_code) {
        case 100:
            s = s + "100 Continue";
            break;
        case 101:
            s = s + "101 Switching Protocols";
            break;
        case 102:
            s = s + "102 Processing";
            break;
        case 200:
            s = s + "200 OK";
            break;
        case 201:
            s = s + "201 Created";
            break;
        case 202:
            s = s + "202 Accepted";
            break;
        case 203:
            s = s + "203 Non-Authoritative Information";
            break;
        case 204:
            s = s + "204 No Content";
            break;
        case 205:
            s = s + "205 Reset Content";
            break;
        case 206:
            s = s + "206 Partial Content";
            break;
        case 207:
            s = s + "207 Multi-Status";
            break;
        case 208:
            s = s + "208 Already Reported";
            break;
        case 226:
            s = s + "226 IM Used";
            break;
        case 300:
            s = s + "300 Multiple Choices";
            break;
        case 301:
            s = s + "301 Moved Permanently";
            break;
        case 302:
            s = s + "302 Found";
            break;
        case 303:
            s = s + "303 See Other";
            break;
        case 304:
            s = s + "304 Not Modified";
            break;
        case 305:
            s = s + "305 Use Proxy";
            break;
        case 307:
            s = s + "307 Temporary Redirect";
            break;
        case 308:
            s = s + "308 Permanent Redirect";
            break;
        case 400:
            s = s + "400 Bad Request";
            break;
        case 401:
            s = s + "401 Unauthorized";
            break;
        case 402:
            s = s + "402 Payment Required";
            break;
        case 403:
            s = s + "403 Forbidden";
            break;
        case 404:
            s = s + "404 Not Found";
            break;
        case 405:
            s = s + "405 Method Not Allowed";
            break;
        case 406:
            s = s + "406 Not Acceptable";
            break;
        case 407:
            s = s + "407 Proxy Authentication Required";
            break;
        case 408:
            s = s + "408 Request Timeout";
            break;
        case 409:
            s = s + "409 Conflict";
            break;
        case 410:
            s = s + "410 Gone";
            break;
        case 411:
            s = s + "411 Length Required";
            break;
        case 412:
            s = s + "412 Precondition Failed";
            break;
        case 413:
            s = s + "413 Payload Too Large";
            break;
        case 414:
            s = s + "414 URI Too Long";
            break;
        case 415:
            s = s + "415 Unsupported Media Type";
            break;
        case 416:
            s = s + "416 Range Not Satisfiable";
            break;
        case 417:
            s = s + "417 Expectation Failed";
            break;
        case 421:
            s = s + "421 Misdirected Request";
            break;
        case 422:
            s = s + "422 Unprocessable Entity";
            break;
        case 423:
            s = s + "423 Locked";
            break;
        case 424:
            s = s + "424 Failed Dependency";
            break;
        case 426:
            s = s + "426 Upgrade Required";
            break;
        case 428:
            s = s + "428 Precondition Required";
            break;
        case 429:
            s = s + "429 Too Many Requests";
            break;
        case 431:
            s = s + "431 Request Header Fields Too Large";
            break;
        case 451:
            s = s + "451 Unavailable For Legal Reasons";
            break;
        case 500:
            s = s + "500 Internal Server Error";
            break;
        case 501:
            s = s + "501 Not Implemented";
            break;
        case 502:
            s = s + "502 Bad Gateway";
            break;
        case 503:
            s = s + "503 Service Unavailable";
            break;
        case 504:
            s = s + "504 Gateway Timeout";
            break;
        case 505:
            s = s + "505 HTTP Version Not Supported";
            break;
        case 506:
            s = s + "506 Variant Also Negotiates";
            break;
        case 507:
            s = s + "507 Insufficient Storage";
            break;
        case 508:
            s = s + "508 Loop Detected";
            break;
        case 510:
            s = s + "510 Not Extended";
            break;
        case 511:
            s = s + "511 Network Authentication Required";
            break;
        }

        s = s + "\r\n"; // other header fields,
        // s = s + "Connection: close\r\n"; // can't handle persistent
        // connections

        //s = s + "Connection: keep-alive\r\n"; // can handle persistent
                                                // connections
        s = s + "Server: JabbaTranslator\r\n"; // server name

        //s = s + "Date: Wed, 01 Mar 2017 17:51:04 GMT\r\n";

        switch (file_type) {
            case 1:
                s = s + "content-type: image/jpeg\r\n";
                break;
            case 2:
                s = s + "content-type: image/gif\r\n";
            case 3:
                s = s + "content-type: application/x-zip-compressed\r\n";
            case 0:
            default:
                s = s + "content-type: text/html\r\n";
                break;
        }
        // if you are missing the Content-Length header on your HTTP response,
        // the HTTP client does not know
        // when the response is complete, so it keeps on waiting for more
        //s = s + String.format("Content-Length : %d\r\n", length);
        s = s + String.format("content-length: %d\r\n", length);
        s = s + "\r\n"; // this marks the end of the httpheader
        //s = s + String.format("content-length : %d\n", length);
        //s = s + "\n"; // this marks the end of the httpheader
        // and the start of the body

		return s;

	}

}


