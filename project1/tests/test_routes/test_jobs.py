import json


def test_create_job(client):
    data = {
        "title": "Software Developer",
        "company": "google",
        "company_url": "www.google.com",
        "location": "Hyderabad, India",
        "description": "python",
        "date_posted": "2022-03-20"
        }
    response = client.post("/jobs/create-job/",json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["company"] == "google"
    assert response.json()["description"] == "python"

def test_read_job_positive(client):
    data = {
        "title": "Software Engineer",
        "company": "yahoo",
        "company_url": "www.yahoo.com",
        "location": "USA,NY",
        "description": "python2",
        "date_posted": "2022-01-09"
        }
    response = client.post("/jobs/create-job/",json.dumps(data))

    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()['title'] ==  "Software Engineer"


def test_read_job_negative(client):

    response = client.get("/jobs/get/10/")
    assert response.status_code == 404