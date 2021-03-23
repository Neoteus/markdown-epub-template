# English

## Pandoc Command

Simple example:

```bash
pandoc -o [OUTPUT_FILE] [INPUT_FILES...]
```

- `-o` *FILE*

  Output to a file, instead of *stdout* by default.

- `--toc`

  Include an automatically generated table of contents in the output document.

- `--resource-path=`*PATH*

  List of paths to search for images and other resources. The paths should be separated by `:` on Linux, UNIX, and macOS systems, and by `;` on Windows. If `--resource-path` is not specified, the default resource path is the working directory. Note that, if `--resource-path` is specified, the working directory must be explicitly listed or it will not be searched. For example: `--resource-path=.:test` will search the working directory and the test subdirectory, in that order.

- `-f` *INPUT_FORMAT*

  `-t` *OUTPUT_FORMAT*

  If input or output format is not specified explicitly, pandoc will attempt to guess it from the extensions of the filenames.

- `--toc-depth=`*NUMBER*

  Specify the number of section levels to include in the table of contents. The default is 3 (which means that level-1, 2, and 3 headings will be listed in the contents).

- `--data-dir=`*DIRECTORY*

  Specify the user data directory to search for pandoc data files. If this option is not specified, the default user data directory will be used. On Linux and Mac OS this will be the pandoc subdirectory of the XDG data directory (by default, `$HOME/.local/share`, overridable by setting the `XDG_DATA_HOME` environment variable). If that directory does not exist, `$HOME/.pandoc` will be used (for backwards compatibility). In Windows the default user data directory is `C:\Users\USERNAME\AppData\Roaming\pandoc`. You can find the default user data directory on your system by looking at the output of `pandoc --version`. A `reference.odt`, `reference.docx`, `epub.css`, `templates`, `slidy`, `slideous`, or `s5` directory placed in this directory will override pandoc’s normal defaults.

- `--epub-embed-font=`*FILE*

  Embed the specified font in the EPUB. This option can be repeated to embed multiple fonts. Wildcards can also be used: for example, `DejaVuSans-*.ttf`. However, if you use wildcards on the command line, be sure to escape them or put the whole filename in single quotes, to prevent them from being interpreted by the shell. To use the embedded fonts, you will need to add declarations like the following to your CSS (see `css` in metadata):

  ```CSS
  @font-face {
  font-family: DejaVuSans;
  font-style: normal;
  font-weight: normal;
  src:url("DejaVuSans-Regular.ttf");
  }
  @font-face {
  font-family: DejaVuSans;
  font-style: normal;
  font-weight: bold;
  src:url("DejaVuSans-Bold.ttf");
  }
  @font-face {
  font-family: DejaVuSans;
  font-style: italic;
  font-weight: normal;
  src:url("DejaVuSans-Oblique.ttf");
  }
  @font-face {
  font-family: DejaVuSans;
  font-style: italic;
  font-weight: bold;
  src:url("DejaVuSans-BoldOblique.ttf");
  }
  body { font-family: "DejaVuSans"; }
  ```

- `--epub-chapter-level=`*NUMBER*

  Specify the heading level at which to split the EPUB into separate “chapter” files. The default is to split into chapters at level-1 headings. This option only affects the internal composition of the EPUB, not the way chapters and sections are displayed to users. Some readers may be slow if the chapter files are too large, so for large documents with few level-1 headings, one might want to use a chapter level of 2 or 3.

- `--epub-subdirectory=`*DIRNAME*

  Specify the subdirectory in the OCF container that is to hold the EPUB-specific contents. The default is `EPUB`. To put the EPUB contents in the top level, use an empty string.


## Markdown Specified for E-Book

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

- `identifier`

  Either a string value or an object with fields `text` and `scheme`. Valid values for `scheme` are ISBN-10, GTIN-13, UPC, ISMN-10, DOI, LCCN, GTIN-14, ISBN-13, Legal deposit number, URN, OCLC, ISMN-13, ISBN-A, JP, OLCC.

- `title`

  Either a string value, or an object with fields `text` and `type`, or a list of such objects. Valid values for `type` are main, subtitle, short, collection, edition, extended.

- `creator`

  Either a string value, or an object with fields `role` and `text`, or a list of such objects. Valid values for `role` are [MARC relators](https://loc.gov/marc/relators/relaterm.html), but pandoc will attempt to translate the human-readable versions (like “author” and “editor”) to the appropriate MARC relators.

- Here are some roles I commonly use:

  - Author [aut]
  - Editor [edt]
  - Illustrator [ill]
  - Translator [trl]

- `contributor`

  Same format as `creator`.

- `date`

  A string value in `YYYY-MM-DD` format (only the year is necessary). Pandoc will attempt to convert other common date formats.

- `lang` (or legacy: `language`)

  A string value in [BCP 47](https://tools.ietf.org/html/bcp47) format. Pandoc will default to the local language if nothing is specified.

  Here are some languages I commonly use:

  - en: English
    - en-US: English with features generally thought to be characteristic of the United States
  - zh: Chinese
    - zh-CN: Chinese as used in China, where the Simplified script is predominant
    - zh-Hans: Chinese as written in the Simplified script
    - zh-Hant: Chinese as written in the Traditional script
    - zh-cmn: Mandarin Chinese
    - zh-yue: Cantonese Chinese
    - zh-gan: Gan Chinese
  - ja: Japanese
    - ja-JP: Japanese as used in Japan

- `subject`

  A string value or a list of such values.

- `description`

  A string value.

- `cover-image`

  A string value (path to cover image).

- `css` (or legacy: `stylesheet`)

  A string value (path to CSS stylesheet).

  A stylesheet is required for generating EPUB. If none is provided using this filed (or the pandoc `-c` option ), pandoc will look for a file `epub.css` in the user data directory (see `--data-dir`). If it is not found there, sensible defaults will be used.

- `page-progression-direction`

  Either `ltr` or `rtl`. Specifies the `page-progression-direction` attribute for the [`spine` element](http://idpf.org/epub/301/spec/epub-publications.html#sec-spine-elem).

- `iBooks`

  iBooks-specific metadata, with the following fields:

  - `version`: (string)
  - `specified-fonts`: true|false (default false)
  - `ipad-orientation-lock`: portrait-only|landscape-only
  - `iphone-orientation-lock`: portrait-only|landscape-only
  - `binding`: true|false (default true)
  - `scroll-axis`: vertical|horizontal|default

- `publisher`

- `type`

- `format`

- `relation`

- `coverage`

- `rights`

### Linked Media

By default, pandoc will download media referenced from any `<img>`, `<audio>`, `<video>` or `<source>` element present in the generated EPUB, and include it in the EPUB container, yielding a completely self-contained EPUB.

If you want to link to external media resources instead, use raw HTML in your source and add `data-external="1"` to the tag with the `src` attribute. For example:

```html
<audio controls="1">
  <source src="https://example.com/music/toccata.mp3"
          data-external="1" type="audio/mpeg">
  </source>
</audio>
```

### The `epub:type` attribute

For epub3 output, you can mark up the heading that corresponds to an EPUB chapter using the `epub:type` attribute. For example, to set the attribute to the value `prologue`, use this markdown:

```MARKDOWN
# My chapter {epub:type=prologue}
```

Which will result in:

```HTML
<body epub:type="frontmatter">
  <section epub:type="prologue">
    <h1>My chapter</h1>
```

Pandoc will output `<body epub:type="bodymatter">`, unless you use one of the following values, in which case either `frontmatter` or `backmatter` will be output:

| section          | body        |
| ---------------- | ----------- |
| prologue         | frontmatter |
| abstract         | frontmatter |
| acknowledgments  | frontmatter |
| copyright-page   | frontmatter |
| dedication       | frontmatter |
| credits          | frontmatter |
| keywords         | frontmatter |
| imprint          | frontmatter |
| contributors     | frontmatter |
| other-credits    | frontmatter |
| errata           | frontmatter |
| revision-history | frontmatter |
| titlepage        | frontmatter |
| halftitlepage    | frontmatter |
| seriespage       | frontmatter |
| foreword         | frontmatter |
| preface          | frontmatter |
| appendix         | backmatter  |
| colophon         | backmatter  |
| bibliography     | backmatter  |
| index            | backmatter  |
