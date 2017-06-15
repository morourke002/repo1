1) create title 
# <title_name>

2) create link

[Link](https://guides.github.com/features/mastering-markdown/)

3) bold words

**bold**

4) itallic words

*italic*

5) Numbered lists

1. One
2. Two
3. Three

6) Bullet points

* Start a line with a star
* Profit!

7) Dashed lines

- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this
  
8) Embed image

![<link_text>](<image_link>)

9) Sub heading

### This is a third-tier heading

#### You can use one `#` all the way up to `######` six for different heading sizes.

10) Quoting

> THERE ARE FOUR LIGHTS!
> - Captain Jean Luc Picard

11 ) In-line code blocks

wrap them in backticks: `var example = true`.  

12) Longer code blocks

    if (isAwesome){
      return true
    }

13) Code 'fencing' (multiple indentations)

```
if (isAwesome){
  return true
}
```

14) Syntax highlighting

```javascript
if (isAwesome){
  return true
}
```

15) Direct commenting

with an @ symbol: Hey @morourk2 — fuck you!

16) Emojis

:sparkles: :camel: :boom:

17) Emphasis continue with underscores (can be combined)

*This text will be italic*
_This will also be italic_

18) More Lists

Unordered

* Item 1
* Item 2
  * Item 2a
  * Item 2b
Ordered

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b

Task Lists

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
If you include a task list in the first comment of an Issue, you will get a handy progress indicator in your issue list. It also works in Pull Requests!

19) Tables - create tables by assembling a list of words and dividing them with hyphens - (for the first row), and then separating each column with a pipe |:

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
Would become:

First Header	Second Header
Content from cell 1	Content from cell 2
Content in the first column	Content in the second column
SHA references

20) Commit Links - use SHA-1 hash will be automatically converted into a Github link

16c999e8c71134401a78d4d46435517b2271d6ac
mojombo@16c999e8c71134401a78d4d46435517b2271d6ac
mojombo/github-flavored-markdown@16c999e8c71134401a78d4d46435517b2271d6ac
Issue references within a repository

Any number that refers to an Issue or Pull Request will be automatically converted into a link.

#1
mojombo#1
mojombo/github-flavored-markdown#1

Automatic linking

Any URL (like http://www.github.com/) will be automatically converted into a clickable link.

Strikethrough

Any word wrapped with two tildes (like ~~this~~) will appear crossed out.

