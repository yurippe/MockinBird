# MockinBird
Rapid prototyping of websites with Jython and Netty

# How to build
```
$> mvn clean package
```
Then locate the jar file in `/target`. The jar file combined with the `lib` folder is all you need to run MockingBird

# How to run
```
$> java -jar MockingBird.jar
```

# From build to doing something
You can have a fully running example by typing
```
$> mvn clean package
$> cd target
$> java -jar MockingBird-0.1.jar
[... starting logs from MockingBird]
>> help
[... help message]
>> run ../Example/Website.py
```
Then navigating to `http://localhost:9000/name/Admin`
