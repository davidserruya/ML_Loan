# Home Lean Project

> This project is an application to determine a client's eligibility for a bank home loan based on a machine learning algorithm.

## Project Tools

> This project uses several technologies:
- Python: for the Machine Learning part.
- Looker Studio: for the visualization of the data through a Dashboard and the Dataset.
- HTML: for the formatting of the application.

## Project Description

> Our case study is based on a dataset of home loan applications composed of multiple fields (gender, marital status, education, monthly salary, loan amount, ...). The objective was to automate the loan eligibility process (real time) based on customer detail provided while filling online application form.
> After testing several supervised learning algorithms, I chose to use the Random Forest algorithm as it was the most efficient.
> This project also includes a dashboard and the whole dataset to better understand the eligibility of applicants.

## Prérequis

The presence of [Python](https://www.python.org/) on the machine is required.

## Build Setup

After cloning this project, you need to run the following commands:

```bash
# Install the streamlit library
$ python -m pip install streamlit
# Install streamlit_option_menu library
$ python -m pip install streamlit_option_menu
# Install the pandas library
$ python -m pip install pandas
# Install the matplotlib library
$ python -m pip install matplotlib
# Installing the sklearn library
$ python -m pip install sklearn
```
## Run Application

> You need to run the command : ``` streamlit run main_page.py ```

## Démonstration

> The application is already online. You can test it by clicking [here]().

## GIT Commands

```bash
# Switch branches or restore working tree files
$ git checkout <name>

# Fetch from and integrate with another repository or a local branch
$ git pull

# Add all files contents to the index
$ git add *

# Record changes to the repository with clean message
$ git commit -m "commit description" 

# Update remote refs along with associated objects
$ git push

# Stash the changes in a dirty working directory away
$ git stash
```

For more explanation about the functioning of this API you can refer to the official documentation below:

- [Python docs](https://docs.python.org/3/).
- [SKLearn docs](https://scikit-learn.org/stable/).
- [Pandas docs](https://pandas.pydata.org/).
- [streamlit docs](https://streamlit.io/).
- [Looker Studio](https://cloud.google.com/looker/docs?hl=fr/).

## Contributor

David Serruya.
