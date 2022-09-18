# Shopping Cart

## Particulars

Version number: 72cf4fe47f85c39779267d0ecee07655a354e623

# Installation instructions

- Install a [Python 3.10 interpreter](https://www.python.org/downloads/).
- To run the tests, run `pytest --cov`. At the time of writing this, here is the result from running the test suite with code coverage.

```
====================================================== test session starts ======================================================
platform win32 -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\antho\PycharmProjects\shopping_cart
plugins: cov-3.0.0
collected 3 items

test_step_1.py .                                                                                                           [ 33%]
test_step_2.py .                                                                                                           [ 66%]
test_step_3.py .                                                                                                           [100%]

---------- coverage: platform win32, python 3.10.4-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
models.py           33      0   100%
test_step_1.py      17      1    94%
test_step_2.py      18      1    94%
test_step_3.py      28      1    96%
------------------------------------
TOTAL               96      3    97%


======================================================= 3 passed in 0.29s =======================================================
```

# Quality assurance

I used `pre-commit` to run the linting and QA checks. If you want to run this manually, you can run `pre-commit run --all-files`. This command is useful if you want to run all the QA functions at once. <br /> But if you want to run it automatically before commits then run `pre-commit install` [or see the pre-commit documentation for other integrations](https://pre-commit.com/#3-install-the-git-hook-scripts).

# Problem statement

As you work through the steps, you’ll create code to allow a user to add products to a shopping cart, calculate the total price, and then the sales tax for the items contained in the cart. As mentioned previously, we are not looking for a command line or a web application, so please just use your tests to drive the code (e.g. class libraries).

Please Note: All totals should be rounded up to 2 decimal places, i.e. 0.565 should result in 0.57 but 0.5649 should result in 0.56. This is basically the same rounding you learned at school, but you can follow this link if you really want more details.

## Assumptions

- Any sales tax applies to the whole shopping cart, and there aren't tax-exempt items in a shopping cart.

## Step 1
Add products to the shopping cart.

Given:
- An empty shopping cart
- And a product, Dove Soap with a unit price of 39.99

When:
- The user adds 5 Dove Soaps to the shopping cart

Then:
- The shopping cart should contain 5 Dove Soaps each with a unit price of 39.99
- And the shopping cart’s total price should equal 199.95

## Step 2

Add additional products of the same type to the shopping cart.

Given:
- An empty shopping cart
- And a product, Dove Soap with a unit price of 39.99

When:
- The user adds 5 Dove Soaps to the shopping cart
- And then adds another 3 Dove Soaps to the shopping cart

Then:
- The shopping cart should contain 8 Dove Soaps each with a unit price of 39.99
- And the shopping cart’s total price should equal 319.92

# Step 3
Calculate the tax rate of the shopping cart with multiple items

Given:
- An empty shopping cart
- And a product, Dove Soap with a unit price of 39.99
- And another product, Axe Deo with a unit price of 99.99
- And a sales tax rate of 12.5%

When:
- The user adds 2 Dove Soaps to the shopping cart
- And then adds 2 Axe Deos to the shopping cart

Then:
- The shopping cart should contain 2 Dove Soaps each with a unit price of 39.99
- And the shopping cart should contain 2 Axe Deos each with a unit price of 99.99
- And the total sales tax amount for the shopping cart should equal 35.00
- And the shopping cart’s total price should equal 314.96


## What we are looking for:
- Test Coverage: The solution should be developed “test-first” and should have excellent unit tests and test coverage. It will be hard to pass this exercise if we can’t reasonably believe the solution was developed “test-first” following TDD.
- Build file: Please provide an automated build file that compiles your code and runs the tests. For java submissions, a Gradle or Maven build file is ideal. Submissions without an automated build will not be accepted.
- Simplicity: We value simplicity as an architectural virtue and a development practice. Solutions should reflect the difficulty of the assigned task and should not be overly complex. Layers of abstraction, patterns, or architectural features that aren’t called for should not be included.
- Self-explanatory code: The solution you produce must speak for itself. Multiple paragraphs explaining the solution are a sign that it isn’t straightforward enough to understand purely by reading code and are not appropriate.
