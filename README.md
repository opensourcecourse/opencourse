# OpenSourceCourse

This is the website for OpenSourceCourse, a short course designed to help engineers and scientists contribute to
the open-source scientific python ecosystem.

The course website is found [here](https://opensourcecourse.dev/).

The website is built with [Quarto](https://quarto.org/).  

# Local Development

First, clone this repo and cd into it. 

```bash
clone git@github.com/opensourcecourse/opencourse

cd opencourse
```

Second, [install quarto](https://quarto.org/docs/get-started/). 

Third, create and activate a virtual environment with [conda](https://docs.conda.io/en/latest/) using the 
environment.yml file included in the repo. 

```bash
conda create -f environment.yml
conda activate opencourse
```

Lastly, render the website

```bash
quarto render .
```
This will create a directory called "_site" which contains an index.html. Double click this to launch the content. 

You can also use Quarto's preview mode to make/view changes live. 

```bash
quarto preview .
```

# Licence

OpenSourceCourse is licenced under GPL v3. 
