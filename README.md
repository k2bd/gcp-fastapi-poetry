# Python + Poetry REST API with FastAPI, hosted on GCP

This template will get you ready to deploy a FastAPI app in Google Cloud with automatic API versioning by major release version and automatic custom domain mapping.

Major tags maintain separate API services in Cloud Run. For example, if my custom domain is `api.k2bd.dev`, running the release GitHub action to create version `v2.3.4` will update the `v2` tag and automatically (re)-deploy to the `v2.api.k2bd.dev` service with the released code. The `v1` service is unaffected, and there's no need to keep `v1`-compatible code around in the default branch of your repo after bumping to `v2`. New `v1` versions can be pushed separately to update that version using whatever workflow you want that produces a new `v1.*.*` semver tag, for example for bugfixes that affect the previous version. This keeps the maintenance cost of the code low while also ensuring old versions of the API are live and available to clients until they're migrated to the newer versions.

## Getting started from the template
1. Rename the `src/gcp_fastapi_poetry` package.
1. Globally replace (*case-sensitive*) instances of `gcp-fastapi-poetry`, `gcp_fastapi_poetry`, and `GCP_FASTAPI_POETRY` with your project and package name (including later in this list).
1. Set your repo up on [CodeCov](https://app.codecov.io/) and add a codecov token to your repo under the `CODECOV_TOKEN` secret.
1. Create a new repo-scoped personal access token and add it as a `DEPLOY_TOKEN` repo secret. This is so we can [maintain major version tags](https://github.community/t/action-does-not-trigger-another-on-push-tag-action/17148/8).
1. Change your Cloud Run configuration in `cloudbuild.yaml` as appropriate. By default, it will deploy an API that can be invoked with no authentication.
1. Configure a Cloud Build trigger in your GCP project to deploy from `cloudbuild.yaml` on a new tag that matches the regex `^(v(\d+))$`, with a substituion variable `_GCP_FASTAPI_POETRY_API_DOMAIN` pointing to the (sub)-domain you want to host the API on. Make sure the cloudbuild service account has the required permissions (Cloud Build settings --> enable Cloud Run, Service Accounts, and Cloud Build) and is [registered as an owner of your custom domain](https://stackoverflow.com/a/70510793) if required.
1. Update `LICENSE.md` as appropriate, making sure to retain the original copyright and permissions notices in your distribution according to the MIT license that this template is distributed under.
1. Create and test your API. Your app under `gcp_fastapi_poetry.api:app` will be hosted on CloudRun when it's deployed.
1. When you're ready to release the first version, run the release GitHub action with the "major" option to deploy `v1` of your API! (or minor/patch to deploy `v0`)
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
- `poe local-server` - Run your API locally

While the local server is running, you can see API docs at `http://localhost:8011/docs` or `http://localhost:8011/redoc`, and can get the OpenAPI spec at `http://localhost:8011/openapi.json`.

### Deployment

Release a new version by manually running the release action on GitHub with a 'major', 'minor', or 'patch' version bump selected.
This will create an push a new semver tag of the format `v1.2.3`, and also update the appropriate major version tag (`v1`, `v2`, ...).

Updating the major version tags will cause Cloud Build to create or update that version's deployment automatically and host it at e.g. `v1.(your configured domain)`. You may need to configure your domain's DNS if you're creating an endpoint for a new major version and you use an external provider. See the domain mappings page linked [here](https://cloud.google.com/run/docs/mapping-custom-domains#map) for instructions.
