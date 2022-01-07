# Python + Poetry REST API with FastAPI, hosted on GCP

## Getting started from the template
1. Rename the `src/gcp_fastapi_poetry` package.
1. Globally replace instances of `gcp-fastapi-poetry` and `gcp_fastapi_poetry` with your project and package name.
1. Set it up on [CodeCov](https://app.codecov.io/) and add a codecov token to your repo under the `CODECOV_TOKEN` secret.
1. Create and test your API. Your app under `gcp_fastapi_poetry.api:app` will be hosted on CloudRun when it's deployed.
1. Change your Cloud Run configuration in `cloudbuild.yaml`. By default, it will deploy an API that can be invoked with no authentication.
1. Configure Cloud Build in your GCP project to deploy from `cloudbuild.yaml` on a new tag push.
1. Update `LICENSE.md` as appropriate, making sure to retain the original copyright and permissions notices in your distribution according to the MIT license that this template is distributed under.
1. When you're ready to release the first version, run the release GitHub action.
1. Remove this section from `README.md`.
1. Happy hacking!

### Like this template?
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png)](https://www.buymeacoffee.com/k2bd)


## Developing

Install [Poetry](https://python-poetry.org/) and `poetry install` the project

### Useful Commands

Note: if Poetry is managing a virtual environment for you, you may need to use `poetry run poe` instead of `poe`

- `poe autoformat` - Autoformat code
- `poe lint` - Linting
- `poe test` - Run Tests

### Releasing

Release a new version by running the release action on GitHub.
