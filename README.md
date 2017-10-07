# Twitter User authenticity
Estimating trustworthiness for a twitter user using a heterogeneous network of twitter

## Setting up the repo
* Clone the repo
* Create a new virtual environment using

		virtualenv -p python3 venv
    
* Activate the virtual environement via
		
		source venv/bin/activate
		
* Install twarc
        
        pip install twarc

* To scrape twitter data

        python src/crawl.py        
