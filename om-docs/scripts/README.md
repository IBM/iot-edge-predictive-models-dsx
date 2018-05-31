# How to use the files in this directory

## Generating PDFs (generate_pdf)

As part of the journey process we must also create PDFs, the file ``README.md`` creates ``overview.pdf``
and ``detailed.md`` creates ``detailed.pdf``. You may then upload these to Wrike, check the files into
the repository, or email them to the publisher you are working with.

### Prereqs

#### Prereq 1: Install git

There are MANY ways to do this and they depend on the operating system you are using. See
[git documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for more details.

If you are using a Mac, the easiest is probably to install the git is to install the Xcode Command
Line Tools. You can do this simply by trying to run ``git`` from a Terminal. If you don’t have it
installed, it will prompt you to install it.

#### Prereq 2: Install Docker

Simply download the [latest stable docker release](https://download.docker.com/mac/stable/Docker.dmg),
and install it as you would any other application. Ensure the docker daemon is running by making sure
you see the docker whale icon in your system tray.

#### Prereq 3: (Optional) Setup SSH key for GHE

This step is only necessary if you plan to check the generated PDFs into the github repository. If
you plan on uploading them to Wrike or emailing them to your publisher, then skip this step.

To push *any* files back to Github Enterprise (github.ibm.com), which is behind our firewall, you'll
need to setup an SSH key to use. We cannot use our w3 username and password combination due to
limitations in Single Sign-On configurations. Don't worry, it's painless and you'll only need to do
it once. It's also all documented [here](https://help.github.com/enterprise/2.10/user/articles/connecting-to-github-with-ssh/).

1. Generate an SSH key

Open a Terminal, paste the text below, substituting in your GitHub Enterprise email address. Click Enter
for all subsequent prompts after that, the defaults are fine. This generates an SSH keypair at ``~/.ssh/id_rsa``
and ``~/.ssh/id_rsa.pub``.

```bash
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
$ Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
$ Enter passphrase (empty for no passphrase): [Type a passphrase]
$ Enter same passphrase again: [Type passphrase again]
```

2. Copy the contents

Output the contents of the public key, and copy it to your clipboard.

```bash
$ cat ~/.ssh/id_rsa.pub
```

3. Add it to your Github Profile

Simply go to the ["SSH and GPG keys"](https://github.ibm.com/settings/keys) option in your Github Settings,
click the "New SSH key" option, give it any name, paste the contents from your clipboard into the text box,
and select "Add key".

### Running the script

Run it by issuing the following command:

```bash
$ ./scripts/generate_pdf 
```

The output shown below should only appear the first time you run the command. Docker is downloading
the image necessary and caching it locally.

```bash
==> generating tmp/readme.pdf
Unable to find image 'jagregory/pandoc:latest' locally
latest: Pulling from jagregory/pandoc
5040bd298390: Pull complete 
7c5f380bbf7c: Downloading [=======================>                           ]  94.59MB/204.2MB
4e1269b776e7: Downloading [========>                                          ]  91.89MB/528.6MB
0f991c8d9b92: Downloading [==============>                                    ]  42.14MB/144.2MB
6a78752096ac: Waiting 
6a78752096ac: Pull complete 
Digest: sha256:d7e72f89543a770053b34509bebc2cd6fe3040fb3c057079dfca3e1164414152
Status: Downloaded newer image for jagregory/pandoc:latest
```

All subsequent calls should look like:

```bash
$ ./scripts/generate_pdf 
==> generating tmp/readme.pdf
==> generating tmp/detailed.pdf
```

#### (Optional) Checking in the PDFs

Once the PDFs have been generated, run the following commands:

```bash
$ git add *.pdf
$ git commit -m "adding PDFs to repo"
$ git push
```
