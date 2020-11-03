# Basics

## Pandoc

The Pandoc command I use:

```bash
pandoc --toc --resource-path=images -o [OUTPUT_FILE] [INPUT_FILES...]
```

`-o` *FILE*

Output to a file, instead of *stdout* by default.

`--toc`

Include an automatically generated table of contents in the output document.

`--resource-path=`*SEARCHPATH*

List of paths to search for images and other resources. The paths should be separated by `:` on Linux, UNIX, and macOS systems, and by `;` on Windows. If `--resource-path` is not specified, the default resource path is the working directory. Note that, if `--resource-path` is specified, the working directory must be explicitly listed or it will not be searched. For example: `--resource-path=.:test` will search the working directory and the test subdirectory, in that order.

## EPUB

### EPUB Metadata

EPUB metadata may be specified using the `--epub-metadata` option, but if the source document is Markdown, it is better to use a YAML metadata block. Here is an example:

```YAML
---
title:
- type: main
  text: My Book
- type: subtitle
  text: An investigation of metadata
creator:
- role: author
  text: John Smith
- role: editor
  text: Sarah Jones
identifier:
- scheme: DOI
  text: doi:10.234234.234/33
cover-image: images/cover.jpg
...
```

### Linked Media

By default, pandoc will download media referenced from any `<img>`, `<audio>`, `<video>` or `<source>` element present in the generated EPUB, and include it in the EPUB container, yielding a completely self-contained EPUB. If you want to link to external media resources instead, see the Advanced part.

Here is an expamble of image:

![doge](../images/example-01.jpg)
