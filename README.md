# Github README.md to HTML 🐍📝

![HTML Example](https://i.imgur.com/kJPjZjG.png "HTML Example")

## Install
``` bash
git clone git@github.com:edmundpf/markdownHtmlGen.git
cd markdownHtmlGen/
pip3 install -r requirements.txt
```

## Usage
### Without included executable
``` python
python3 gitHtmlMaster.py -u https://github.com/myName/myRepoName -f myFilename
```
### With included executable
``` bash
./html -u https://github.com/myName/myRepoName -f myFilename
```

## CLI flags
* -u, --url
  * **Choose Github repo url** by entering URL
  * `-u https://github.com/edmundpf/markdownHtmlGen`
* -f, --file
  * **Choose destination filename** by entering filename
  * Files are saved in the _markdownHtmlGen/files/_ directory as an HTML file with respective naming
    * If no named specified, filename will match the Github repo name
  * `-f fluffyKittens`
## Contributing
  * If you wish to contribute to the project, please submit a pull request! Thanks!
  
