# Guide to Implementing a dataset

## Pre-Requisites

- A working installation of Git
- A GitHub Account
- Python 3.8 or higher
- Poetry 1.3.1

## Contributing a new Dataset

### 1. Setting up the repository

#### 1.1 Forking the project
Fork the [image_datasets](https://github.com/karthikrangasai/image_datasets) repository to your local github account.

#### 1.2 Forking the project

After forking the project, clone the project locally using the one of the following commands:

```bash
$ git clone git@github.com:<your_github_username>/image_datasets.git      # If using SSH

$ git clone https://github.com/<your_github_username>/image_datasets.git  # If using HTTPS
```

Enter the project directory once the project has been cloned locally.

```bash
$ cd image_datasets  # enter the directory
```

#### 1.3 Set up appropriate remotes

Cloning a repository auto creates the `origin` remote for the project which enables to push/pull to the forked repository.

To enable receiving the latest project updates, it is necessary to setup another remote generally named as `upstream`. This also helps in submitting Pull Requests.

Use one of the following commands:

```bash
$ git remote add upstream git@github.com:karthikrangasai/image_datasets.git      # If using SSH

$ git remote add upstream https://github.com/karthikrangasai/image_datasets.git  # If using HTTPS
```


To verify that the remote has been added, run the following command and verify the outputs: (HTTPS version accordingly)

```bash
$ git remote -v
origin  git@github.com:<your_github_username>/image_datasets.git(fetch)
origin  git@github.com:<your_github_username>/image_datasets.git (push)
upstream    git@github.com:karthikrangasai/image_datasets.git (fetch)
upstream    git@github.com:karthikrangasai/image_datasets.git (push)
```

#### 1.4 Keep the local branches up-to-date

It is necessary to `fetch` the latest changes from the `upstream` remote to work the latest version of the project.

```bash
$ git fetch upstream
```

The `git fetch` command fetches the latest code from all the branches on the `upstream` remote and saves it locally.

To apply these changes to the local copy, it is required to `rebase` the local branch with the `upstream` branch.

```bash
$ git checkout master          # To ensure that the destination branch is correctly set
$ git rebase upstream/master   # Apply the latest changes to the local `master` branch
```

**NOTE:** `rebase` assumes the destination branch as the current local branch and applies the changes from the branch provided in the command.

#### 1.5 Making new changes

Before you make changes, you should always create a new branch to implement your changes.

Running the following command creates a new branch from the current branch and its current state:

```bash
$ git checkout -b feature/<dataset_name>
```

**NOTE:** <b style="color:red"> Please do not make changes on the master branch! </b>


To ensure that changes are being made on the right branch, run the following command:

```bash
$ git branch
```

The correct branch will have a asterisk <b style="color:red"> \* </b> in front of it.

### 2. Creating a development environment
This project uses the [`poetry`](https://python-poetry.org) dependency management tool. Ensure that a working installation of poetry 1.2.1 or above is installed.

Creating a virtual environment with `poetry` is as easy as running the following command:

```bash
$ poetry install --all-extras
```

This aforementioned command creates a virtual environment, installs all the dependencies, and also editable installs the project to reflect the changes during development.

### 3. Implement your dataset

**NOTE:** Ensure that you are on the right branch using the approach mentioned previously.

This project leverages the features provided by the [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) package for templating a common script to be used by all the dataset loaders.

To add a new dataset loading script, run the following command to pre-populate the directory and files along with some biolerplate code.

The script will take a few inputs interactively and generate the necessary files.

```bash
cookiecutter templates --output-dir src/image_datasets/datasets
```

### 4. Check if your dataloader works

Make sure your dataset is implemented correctly by checking in python the following commands:

```python
from datasets import load_dataset

data = load_dataset("src/image_datasets/datasets/<dataset_name>/<dataset_name>.py", name="<dataset_name>")
```

Run these commands from the top level of the `image_datasets` repo (i.e. the same directory that contains the `pyproject.toml` file).

<!-- Once this is done, please also check if your dataloader satisfies our unit tests as follows by using this command in the terminal:

```bash
python -m tests.test_bigbio bigbio/biodatasets/<dataset_name>/<dataset_name>.py [--data_dir /path/to/local/data]
```

Your particular dataset may require use of some of the other command line args in the test script.
To view full usage instructions you can use the `--help` command,

```bash
python -m tests.test_bigbio --help
``` -->

### 5. Format your code (**Run these commands in your custom branch**)

Add the files that have been changed/added to the index and call the pre-commit runner to format the files.

Add the files back to the index incase the tools like `black` or `isort` make any changes.

Some errors pointed by `flake8` and `mypy` will need manual resolving.

```bash
$ pre-commit run --verbose  # Runs multiple checks and formats the code.
```

### 6. Commit your changes (**Run these commands in your custom branch**)

When `pre-commit` runs successfully, the files can be committed.

```bash
$ git commit -m "A message describing your commit"
```

**NOTE:** It is recommended to fetch and rebase the local repository with the latest changes from the `upstream` remote at this point. Refer to section `1.4` for that.

Push these changes to **your fork** with the following command:

```bash
$ git push origin feature/<dataset_name>
```

### 7. Make a pull request

Make a Pull Request to implement your changes on the main repository [here](https://github.com/karthikrangasai/image_datasets/pulls).

To do so, click "New Pull Request". Then, choose your branch from your fork to push into "base:master".

When opening a PR, please link the [issue](https://github.com/karthikrangasai/image_datasets/issues) corresponding to your dataset using [closing keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) in the PR's description, e.g. `resolves #17`.
