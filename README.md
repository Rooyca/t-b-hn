# URL Check with Auth

[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Lint/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)
[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Integration%20Test/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)

This is a GitHub action that allows you to check the status of a url with authentication. For now is just a post request, although in the future the idea is to add the option to select different methods.

## Usage

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `URL`  | The url to which the request is to be made     |
| `USER`   | Username for authentication    |
| `PASSW`   | Password for authentication    |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `Status`  | Code status from request (returns 200)    |
| `Response`  | Result of request (returns 'Everything is ok!')    |


### Example workflow

```yaml
name: My WF
on:
  schedule:
    # Runs every six hour
    - cron: '0 */6 * * *'
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action
      id: myaction

      uses: rooyca/t-b-hn@master

      with:
        URL: ${{ secrets.URL }}
        METHOD: "POST"
        AUTH: true
        USER: ${{ secrets.USER }}
        PASSW: ${{ secrets.PASSW }}
    - name: Check outputs
      run: |
        echo "Results - ${{ steps.myaction.outputs.Response }}" &&
        echo "Code - ${{ steps.myaction.outputs.Status }}"
```

## Development v1.2

- [x] Add methods
- [ ] Add multiple url
- [x] Add option to request without Auth
