# URL Check with Auth

[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Lint/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)
[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Integration%20Test/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)

This is a GitHub action that allows you to check the status of a url with authentication. For now is just a post request, although in the future the idea is to add the option to select different methods.

## Usage

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action

      # Put your action repo here
      uses: rooyca/url-check-with-AUTH@master

      # Put an example of your mandatory inputs here
      with:
        URL: http://example.com
        USER: username
        PASSW: password
```

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

## Development v1.2

- [ ] Add methods
- [ ] Add multiple url
- [ ] Add option to request without Auth
