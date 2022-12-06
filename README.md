# [Donatify](https://github.com/TejasPrabhu/Donatify)

[![GitHub](https://img.shields.io/github/license/agupta15k/ncsu_se_fall22_22_pr_1?color=green&label=license&logo=MIT)](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/blob/main/LICENSE.md)
[![GitHub issues](https://img.shields.io/github/issues-raw/agupta15k/ncsu_se_fall22_22_pr_1)](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/issues)
[![Github closed issues](https://img.shields.io/github/issues-closed-raw/agupta15k/ncsu_se_fall22_22_pr_1)](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/issues?q=is%3Aissue+is%3Aclosed)
[![Github pull requests](https://img.shields.io/github/issues-pr/agupta15k/ncsu_se_fall22_22_pr_1?color=red)](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/pulls)
[![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/agupta15k/ncsu_se_fall22_22_pr_1?color=blue)](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/pulls?q=is%3Apr+is%3Aclosed)
[![Github all contributors](https://img.shields.io/github/contributors/agupta15k/ncsu_se_fall22_22_pr_1?color=green)](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/graphs/contributors)
[![DOI](https://zenodo.org/badge/557621983.svg)](https://zenodo.org/badge/latestdoi/557621983)
[![codecov](https://codecov.io/gh/TejasPrabhu/Donatify/branch/main/graph/badge.svg?token=y7kqfbG9mX)](https://codecov.io/gh/TejasPrabhu/Donatify)

This project is an extension of the previous work : [Donatify](https://agupta15k.github.io/ncsu_se_fall22_22_pr_1/)

The gift of giving always comes full circle. Giving and receiving go hand in hand, and being generous is a selfless act. F feeling good about contributing is one of the main benefits of giving. Giving back to people in need allows you to grow personally and gives you a higher sense of fulfillment. It also makes you feel good to serve others. You may donate that extra food or that unused item to someone in need rather than throwing it trash or stashing it at the back of the storehouse. Knowing that you're contributing much-needed resources to a worthwhile cause for those in need gives you a sense of self-worth. You and your loved one will also feel good about helping others, which is an added bonus.

## Demo video

https://user-images.githubusercontent.com/112216701/194792312-64c5dea3-24a1-4a61-942c-df805e35800a.mp4

## App in action

registration with OTP and Login:


Donate an item:


Marketplace:


## Getting started

- ### Prerequisites
  - [npm](https://www.npmjs.com/) and [node](https://nodejs.org/en/) (version 16.X or 16.17.1) should be installed.
  - Make sure the database server (mysql) is on. Consider using XAMPP.
  - Download [Python3](https://www.python.org/downloads/).
  - pytest for testing the application server.

- ### Dependencies

  **Backend**: [flask](https://flask.palletsprojects.com/en/2.2.x/) (2.2.2), [flask_cors](https://flask-cors.readthedocs.io/en/latest/) (3.0.10), [json](https://docs.python.org/3/library/json.html), [asyncio](https://docs.python.org/3/library/asyncio.html), [ast](https://docs.python.org/3/library/ast.html), [re](https://docs.python.org/3/library/re.html), [mysql](https://dev.mysql.com/doc/connector-python/en/) (8.0.30), [pytest](https://docs.pytest.org/en/7.1.x/) (7.1.2), [pdoc](https://pdoc.dev/) (0.10.0).
  
  **Frontend**: [axios](https://axios-http.com/docs/intro) (1.0.0), [antd](https://ant.design/docs/react/introduce) (4.23.4), [jsdoc](https://jsdoc.app/) (3.6.11), [react-select](https://react-select.com/home) (5.4.0), [react-tag-input](https://www.npmjs.com/package/react-tag-input) (6.8.1), [reactstrap](https://www.npmjs.com/package/reactstrap) (9.1.4), [jest](https://jestjs.io/).

- ### Installation and Run

    **Backend**: [Documentation](https://htmlpreview.github.io/?https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/blob/backendDocs/index.html)

    1. Create virtual environment

    ```
    python -m venv <name_of_virtualenv>
    ```

    2. Activate Python Virtual environment

    ```
    <name_of_virtualenv>\Scripts\activate.bat for Windows users.
    source <name_of_virtualenv>/bin/activate for linux users.
    ```

    3. Install dependencies

    ```
    pip install -r requirements.txt
    ```

	4. Make sure the database is imported from ```src/database/donationsystem.sql``` onto the mysql server.
	
    5. Run the below command from the main directory to start the backend application server.

    ```
    python -m src.Backend.app
    ```

    6. The backend flask application will be up and running at ```localhost:5001```

    **Frontend**: [Documentation](https://htmlpreview.github.io/?https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/blob/frontendDocs/left-overs/0.1.0/index.html)

    1. After cloning the repository, move to the directory ```src\frontend``` where our frontend code is located.

    2. Install all the dependencies using npm. Command to run: ```npm install```. This will fetch the dependecies from package.json file, and install them.

    3. Start the server by using the command ```npm start```. This will run the server on port ```3000```, and the website can be accessed by going to ```http://localhost:3000/```.

    4. If credentials of a registered user are available, use them, or register a new user and interact with the website.
  
 - ### Testing

    **Backend**

    1. Run the below command from the main directory. This should run all the test cases for app.py.

    ```
    pytest
    ```
    
    **Frontend**

    1. Move to the directory ```src\frontend``` where our frontend tests are located.
    
    2. Run the tests using the command ```npm test -- --coverage --watchAll=false```. This will run all the tests across the frontend code.


  - ### Troubleshooting
  
    Try the following troubleshooting steps. If none of them work, contact the repository owner/file an issue.

    **Backend**

    1. We have added the print statements in all of the backend functions to know execution of the codes.
    2. In case of error the print statements do let us know about the issue of code break.
    3. The api responses the status code, valid message and response header which they can share back for troubleshooting.

    **Frontend**
    
    1. Since frontend is build using JavaScript, React and Redux, check for console logs under developer tools to identify any failures.
    2. Consider installing and using [React developer tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) and [Redux developer tools](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?hl=en) to track the request through the system.

## Directory structure

    .
    ├── .github
    |   ├── workflows
    |   |   ├── frontendGitActions.yml      # GitActions workflow for frontend
    |   |   ├── backendGitActions.yml       # GitActions workflow for frontend
    ├── .vscode
    |   ├── extensions.json                 # Recommended extensions for vscode
    |   ├── settings.json                   # Workspace settings for vscode
    ├── docs
    |   ├── Rubrics
    |   |   ├── proj1rubric.md              # Project rubric
    |   ├── Backend                         # Documentation for backend
    |   ├── frontendDocs/left-overs/0.1.0   # Documentation for frontend
    |   ├── README.md                       # Readme file for docs folder
    ├── src
    |   ├── Backend
    |   |   ├── __init__.py                 # Init file for backend
    |   |   ├── app.py                      # File containing backend APIs
    |   |   ├── dbconfig.py                 # DB configuration for backend
    |   |   ├── utils.py                    # Utilities for backend
    |   ├── database
    |   |   ├── donationsystem.sql          # Backend SQL
    |   ├── frontend
    |   |   ├── public                      # Folder containing assets and images
    |   |   ├── src
    |   |   |   ├── API                     # Folder containing API calling frontend code
    |   |   |   ├── __tests__               # Folder containing unit tests for frontend
    |   |   |   ├── app                     # Folder containing redux store configuration
    |   |   |   ├── components              # Folder containing frontend react components
    |   |   |   ├── containers              # Folder containing containers to connect components with redux store
    |   |   |   ├── reducers                # Folder containing reducers
    |   |   |   ├── axiox.js                # API client generation
    |   |   |   ├── index.css               # CSS configuration for frontend
    |   |   |   ├── index.js                # Entry point for frontend
    |   |   |   ├── leftOver.jsx            # Root react component
    |   |   |   ├── setupTests.js           # Setup jest configuration for unit testing
    |   |   ├── .eslintignore               # Ignore configuration for eslint
    |   |   ├── .eslintrc.js                # eslint configuration
    |   |   ├── package.json                # Package configuration and dependency closure
    |   ├── README.md                       # Readme file for src folder
    ├── test
    |   ├── README.md                       # Readme file for test folder
    |   ├── __init__.py                     # Init file for test folder
    |   ├── test_app.py                     # Tests for backend
    ├── .gitattributes                      # File for git attributes
    ├── .gitignore                          # File for git ignore
    ├── CODE_OF_CONDUCT.md                  # Code of conduct for repository
    ├── CONTRIBUTING.md                     # Details about contributing to the repository
    ├── LICENSE.md                          # MIT License details
    ├── README.md                           # Readme file for repository
    ├── requirements.txt                    # Details of dependency packages
    └── setup.py                            # Setup file for the module

## Releases

* [Donatify v0.1](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/releases/tag/v0.1): Initial v0.1 release
* [Donatify v1.0.0](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/releases/tag/v1.0.0): First major release
* [Donatify v1.0.1](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/releases/tag/v1.0.1): Minor version release
* [Donatify v1.0.2](https://github.com/agupta15k/ncsu_se_fall22_22_pr_1/releases/tag/v1.0.2): Minor version release

## Roadmap

* Roadmap for this project can be found [here](https://github.com/users/TejasPrabhu/projects/2).

## Chat channel

* All the communication was handled through a private chat channel, online and offline meets. Some screenshots of discussions can be found [here](https://github.com/TejasPrabhu/Donatify/tree/main/docs/chatChannel/screenshots).

## Support
We do our best to answer all tickets in a timely manner, but sometimes we accumulate a backlog and may take awhile to respond. Please be patient—we will get back to you as soon as we can! 
Please do contact any of us:
* Kartik Rawool(khrawool@ncsu.edu)
* Naveen Jayanna(njayann@ncsu.edu)
* Samarth Purushothaman(spurush@ncsu.edu)
* Tejas Prabhu(tprabhu2@ncsu.edu)
* Shubham Loya(ssloya@ncsu.edu)

## License
* We are using [MIT license](https://github.com/TejasPrabhu/Donatify/blob/main/LICENSE.md)
* Copyright (c) 2022 Group 45

## Contributors ✨

Thanks goes to these wonderful people.
<table>
  <tr>
    <td align="center"><a href="https://github.com/kartikrawool"><img src="https://avatars.githubusercontent.com/u/55804665?v=4" width="100px;" alt=""/><br/><sub><b>Kartik Rawool</b></sub></a></td>
    <td align="center"><a href="https://github.com/Naveen-Jayanna"><img src="https://avatars.githubusercontent.com/u/52947925?v=4" width="100px;" alt=""/><br/><sub><b>Naveen Jayanna</b></sub></a></td>
    <td align="center"><a href="https://github.com/samarth-p"><img src="https://avatars.githubusercontent.com/u/42717178?v=4" width="100px;" alt=""/><br/><sub><b>Samarth Purushothaman</b></sub></a></td>
    <td align="center"><a href="https://github.com/TejasPrabhu"><img src="https://avatars.githubusercontent.com/u/100992314?v=4" width="100px;" alt=""/><br/><sub><b>Tejas Prabhu</b></sub></a></td>
    <td align="center"><a href="https://github.com/crmgogo"><img src="https://avatars.githubusercontent.com/u/55990000?v=4" width="100px;" alt=""/><br/><sub><b>Shubham Loya</b></sub></a></td>
  </tr>
</table>
