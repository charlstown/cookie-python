# Contributor Guidelines

Thanks for your interest in contributing to PyTemplate. This page will give you a quick overview of how things are
organized and, most importantly, how to get involved. Everyone is welcome to contribute, and everybody's 
contribution is valued.

## 0. Before contributing
Welcome to PyTemplate! Before sending your pull requests, make sure that you read the whole guidelines.
If you have any doubt on the contributing guide, please feel free to state it clearly in an issue against the
repository.



## 3. Submitting changes

1. Create an issue.
2. Assign the issue to a developer and create a branch.
3. Create a Pull Request.
4. The admin (first creator) of the repository will review the Pull Request.

### Git branches

- Always perform work in a feature branch.
- It is better to branch out from `develop` branch.
- Delete local and remote feature branches after merging.

### Git commit messages

- Start the subject with an action between brackets. Ex.: `[fix]`.
- Separate the subject from the body with a newline between the two (if the body exists).
- Limit the subject line to 50 characters and Wrap the body at 72 characters.
- Capitalize the subject line.
- Do not end the subject line with a period.
- Use imperative mood in the subject line.

#### Commit actions

| Actions  | Example                                       | Description                                           |
|----------|-----------------------------------------------|-------------------------------------------------------|
| `update` | `[update]` secret added to the config-service | A commit in the code that doesn't change the outcome. |
| `fix`    | `[fix]` string error                          | A commit pushed to fix a previous bug in the code.    |
| `delete` | `[delete]` ignored folder in new version      | A commit with file deletions.                         |

Example:

```sh
git commit -m "[Update] get initial documentation"
```

(If applied, this commit will be `[update] get initial documentation`)


## Thank you!

If you have any questions, concerns or comments about these guidelines, please get in touch. You can do this by raising
an issue against the template repository here: https://github.com/charlstown/py-template

Happy coding!

-- @charlstown