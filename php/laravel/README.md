# Laravel

## Setup


a) w/ COMPOSER CREATE PROJECT

```bash
$ composer create-project --prefer-dist laravel/laravel myapp 8.0.0 # ... // 8.0.*
$ php artisan key:generate # ... // Set application key to a random string
$ sudo chmod -R 0777 storage bootstrap/cache # ... // Directories within the storage and the bootstrap/cache directories should be writable by your web server.
```

b) w/ LARAVEL INSTALLER  

```bash
$ composer global require laravel/installer # ... // Download the Laravel installer using Composer. Make sure to place composer's system-wide vendor bin directory in your $PATH so the laravel executable can be located by your system: GNU / Linux Distributions: $HOME/.config/composer/vendor/bin
$ laravel new blog # ... // Once installed, the laravel new command will create a fresh Laravel installation in the directory you specify. For instance, "laravel new blog" will create a directory named blog containing a fresh Laravel installation with all of Laravel's dependencies already installed.
```

c) w/ DOCKER

```text
https://github.com/Janis-Rullis-IT/lara8-vue3-api? laravel8, php8, docker-compose, vue3, vue-cli5, ts4
```

php > laravel > ROUTE > SETUP  
php > laravel > CONTROLLER  

\0
