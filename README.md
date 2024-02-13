# module_3.6_step10
# install dependencies into your virtual envirinment if needed
pip install -r requirements.txt

# Run the following test:
pytest --language=es test_items.py

assessment criteria:
- pytest --language=es, test passes.
- Check for different languages.
  Add time.sleep(30) command after opening a link. 
  Run the test with parameter --language=fr and visually check that the button text is "Ajouter au panier".
- Browser shall be declared in browser fixture and be passed to the test as a parameter.
- The test check whether the button to add to basket is present. The selector is unique for the page. There is assert.
- The method name inside test_items.py correspondes to the task. test_something name doesn't meet the requirement.
