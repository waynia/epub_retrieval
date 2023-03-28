English | [简体中文](https://github.com/waynia/epub_retrieval/blob/master/readme.zh-CN.md)

## Target of this project

This demo project is aimed to parse personal e-book library using Open AI APIs. Its input is a epub format e-book, and its output is a .csv file with the summary of the segments as well as the main idea of the input book. Also, the functions in this project provides the search function based on embedding similarites in embedding_lib.py file. Up till now, limited by the time that I could spend on this spare-time work, I only finished the core part, which invokes the API to parse one book with .epub format in a given path, and output the recursive summary of the whole book. 

The next part of this work, is to make it become a [Calibre e-book management application](https://calibre-ebook.com/) plugin, and help every one to get new ideas from their book collections. Also, if possible, to become an infrastructure to construct some specific-knowledge-based web apps.

## Characteristics of this work 

Noticing that this work differs from those other information retrieval ones. 

Firstly, I divided the text of the e-book into groups by chapters and sub-chapters, which means we could summarize e-books with their naturally organized ways. Every sentence in the book is also not interrupted and subdivided into different chunks by the limit of prompt length, which preserves the valid information during parsing.

Secondly, the summary is recursive. This work summarizes the given book from every basic sentence, to a paragraph, then to the block consisting of several neighboring paragraphs, and then to a whole chapter, and finally to the whole book. Using the summary as the context during chat with GPT, we can get the details as well as the whole insight from the book.

What's more, the code of this project is well-organized. The entrance of this project is the main.py, in which only a few parameters should be set. The functions used for data filtering and information extracting is in book_parser.py,  and the functions used for summarizing is in the summary_lib.py. The functions in these two files invoke some low-level functions in prompt_lib.py and embedding_lib.py. All the configurations are in the config.py.

## Waiting for your joining

I guess this work is very promising to become a common tool for miscellaneous purposes, such as a Chat-GPT plugin, or an assistant for academic research. If you feel interested, you could download this work and do whatever you want, or consider to join me to construct some useful apps. The code is heavily commented and is ready for your study. Best wishes to you.

## Demo
This is a snapshot of this project to recursively summarize the content of the book ***Chimpanzee Politics*** in Chinese version.
![image](https://user-images.githubusercontent.com/49633741/228145703-5b20c39e-119b-4af5-8327-060fa06e0712.png)
