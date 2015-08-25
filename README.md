# docker-compose-openfalcon
Run all Open-Falcon components in docker engine.

## config
You need to configure two file _conf/fe.json_ and _conf/portal.py_ .

In _conf/fe.json_, replace **192.168.1.100** with your host IP in line 31, 32 and 33.

In _conf/portal.py_, replace **192.168.1.100** with your host IP in line 19 and 20. If you have more than two network interface, you can replace with internal IP in line 19, and external IP in line 20.

## Run

Initialize databases.
```
$sudo docker-compose -f init.yml up -d
```

After 10 seconds, run all Open-Falcon components.
```
$sudo docker-compose -f docker-compose.yml up -d
```
