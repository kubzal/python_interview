build:
	docker build -t python_interview .
run:
	docker run -d -p 5000:5000 python_interview