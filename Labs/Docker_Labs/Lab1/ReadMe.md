docker build -t lab1:v1 .

docker save lab1:v1 > my_image.tar

docker run lab1:v1

I had changed the dataset to wine dataset, used Logistic Regression Model and ran these docker commands successfully.
