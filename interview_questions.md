# Docker

#### Docker RUN vs CMD vs ENTRYPOINT

* RUN executes command(s) in a new layer and creates a new image. E.g., it is often used for installing software packages.
* CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
* ENTRYPOINT configures a container that will run as an executable.

```
RUN apt-get install python3
CMD echo "Hello world"
ENTRYPOINT echo "Hello world"
```

#### Docker COPY vs ADD

* COPY and ADD are both Dockerfile instructions that serve similar purposes. They let you copy files from a specific location into a Docker image.
* COPY takes in a src and destination. It only lets you copy in a local file or directory from your host (the machine building the Docker image) into the Docker image itself.
* ADD lets you do that too, but it also supports 2 other sources. First, you can use a URL instead of a local file / directory. Secondly, you can extract a tar file from the source directly into the destination.

#### Difference between an Array and String Based CMD

* The official terms for this are exec form and shell form commands. Both do nearly the same thing, but there's an important difference.
* Using [] is considered “exec form” and the plain string command is considered "shell form"
* Exec Form runs your CMD’s binary as is, along with any arguments you optionally pass in.

```
CMD ["gunicorn", "-c", "python:config.gunicorn", "hello.app:create_app()"]
```
* Shell Form runs your CMD’s binary through a shell which has the added benefit of using any shell functionality you want (such as using pipes and &&, etc.).

```
CMD gunicorn -c "python:config.gunicorn" "hello.app:create_app()"
```
* Which One Should You Use?

Shell form sounds better in theory, but it can mess with signal processing. It also means the shell process ends up being PID 1 instead of whatever binary you’re running in your CMD.

```
Showing what PID 1 is using both methods:
# The output of `ps` when you use exec form:
PID   USER     TIME   COMMAND
  1   root     0:00   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
 15   root     0:02   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
188   root     0:00   ps

# The output of `ps` when you use shell form:
PID   USER     TIME   COMMAND
  1   root     0:00   /bin/sh -c gunicorn -c python:config.gunicorn hello.app:create_app()
  6   root     0:00   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
 16   root     0:00   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
 29   root     0:00   ps
```
Docker (and I) both recommend that you use exec form whenever possible, which really is most of the time. If you need to do complicated shell scripting when a container starts, you should probably use an ENTRYPOINT script.

But what about Docker Compose:
* If you’re curious, Docker Compose appears to convert shell form into exec form by splitting your command: by spaces. I didn’t look at the source code to see if this is the full story, but I did notice that PID 1 is still gunicorn when using the custom command listed below:
```
    command: >
      gunicorn --reload -c "python:config.gunicorn" "hello.app:create_app()"
```
* The official Docker Compose documentation says it supports the [] syntax too if you want to be more explicit. If anyone knows the exact story behind this, please leave a comment below and I’ll update the post. 

