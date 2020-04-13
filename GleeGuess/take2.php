<?php
function displayRandomPhotoArea()
{
    $photoAreas = array("1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg");

    $randomNumber = array_rand($photoAreas);
    $randomImage = $photoAreas[$randomNumber];

    echo "<img src=\"$randomImage\" width=\"131\" height=\"192\">";
}

displayRandomPhotoArea();
?>
