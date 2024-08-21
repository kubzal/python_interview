build:
	docker build -t python_interview .
run:
	docker run -d -p 5000:5000 --name python_interview python_interview:latest

stop:
	docker rm -f python_interview