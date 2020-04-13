<?php
	$pic = array('1.jpg','2.jpg','3.jpg','4.jpg','5.jpg');
	shuffle($pic);
?>
<html>
  <head>
    <title>Glee Guess Who </title>
  </head>
  <body>
    <ul>
    <?php
              for( $i=0; $i<4; $i++)
                    echo "<li style=\"display:inline;\">
                              <imgsrc=\"$pic[$i]\" width=\"131\"height=\"192\">
                            </li>";
    ?>
</ul>
  </body>
</html>
