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
$> java -jar MockingBird-0.2.jar
>> start 9000
[... starting MockingBird on port 9000]
>> start socketio 0.0.0.0 9092
[... starting socketio on port 9092]
>> run ../Example/Website.py
[... Replaced the Jetty handler, and an example website now works]
>> runasync ../Example/EventGenerator.py
[... Broadcast 1000 events with random intervals of [0..5] seconds]
[    (can be seen on page http://localhost:9000/socketio ]
```
Then navigating to `http://localhost:9000/name/Admin` or `http://localhost:9000/socketio`
