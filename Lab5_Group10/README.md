
# Lab 5: Selenium Python API for Element Interaction

---

## Overview

This lab assignment involves creating a Selenium test automation script using Python to simulate an online shopping process. The automation will interact with the demo website: [Magento Software Testing Board](https://magento.softwaretestingboard.com/). The goal is to validate the shopping workflow—from selecting a dress to verifying that the order summary in the shopping cart correctly displays the chosen item.

---

## Assignment Description

In this lab, you will:
1. **Setup and Naming Conventions:**
   - Create a new Selenium IDE project named `Lab5_GroupN` (replace `N` with your actual group number).
   - The Python test file must follow the naming format: `Lab5_firstname1_firstname2.py`.

2. **Test Automation Requirements:**
   - **Navigation:** Begin by clicking through the website’s menu: Women -> Tops -> Hoodies & Sweatshirts.
   - **Product Selection:** Filter products by selecting specific attributes (e.g., Style: Pullover, Size: M, Price: $50.00 - $59.99, Color: Purple, Material: Polyester). You might need to use tools like ChroPath to locate elements correctly.
   - **Adding to Cart:** Choose a dress (if multiple options are available) and click the "Add to Cart" button. Note that this may require switching to a frame.
   - **Cart and Checkout Process:** 
     - Click on the cart icon.
     - Click the "Proceed to Checkout" button.
   - **Verification:** Assert that the "Order Summary" displays the dress you selected.
   - **Cleanup:** Close the browser after completing the steps.

3. **Coding and Test Design:**
   - Use test-case fixtures to organize your tests.
   - Include descriptive comments in your code, explaining each action and web element selection.
   - It is recommended to break down the entire shopping process into multiple test cases instead of a single test case.

4. **Presentation and Submission:**
   - Record a video demonstrating the test process on the website as well as a walkthrough of your code.
   - Both lab partners should explain their role and the task distribution.
   - Submit the zipped project file along with your video recording.

---





