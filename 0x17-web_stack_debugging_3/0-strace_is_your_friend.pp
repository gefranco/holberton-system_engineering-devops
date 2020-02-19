# fix wp by replacing phpp with the correct one
exec { 'fix wp':
  command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
}
