<?php
if (isset($_GET["speed"])) {
	file_put_contents("sliderspeed", htmlspecialchars($_GET["speed"]));
	die(htmlspecialchars($_GET["speed"]));
} else {
	die("Fehler!");
}
?>