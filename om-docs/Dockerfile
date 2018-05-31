FROM conoria/alpine-pandoc:latest

ADD . /source

ENTRYPOINT pandoc Detailed.md -o /output/Detailed.pdf -fmarkdown-implicit_figures
