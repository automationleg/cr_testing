FROM python:3.9.6

COPY . /
# install python packages
RUN pip install -r requirements.txt

CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "test_reports"]
