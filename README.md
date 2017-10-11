# Twitter User authenticity
Estimating trustworthiness for a twitter user using a heterogeneous network of twitter

## Setting up the repo
* Clone the repo
* Create a new virtual environment using
  ```
  virtualenv -p python3 venv
  ```
* Activate the virtual environement via
  ```
  source venv/bin/activate
  ```      
* Install twarc
  ```
  pip install twarc
  ```
* To scrape twitter data
  ```
  python src/crawl.py        
  ```

## MongoDB schema

* Database name : ```twit_user_auth```
* Only one collection type : ```twitusers```
* Fields in ```twitusers``` :  
  * ```user_id```
  * ```user_handle```
  * ```authenticity_score``` : Value between 0 to 1
  * ```manual_tag``` : Can be 0 (not alloted / not sure) / -1 (not credible) / 1 (credible user)
