from book_parser import epub_parser
from summary_lib import *
import openai

# Parameters you should input
openai.api_key = "Your OpenAI API Key"  # 连接openai的验证key
summary_file_name = 'path/to/your/csv/file/for/storing/summaries'  # 存放summary文字的
book_name = '/path/to/your/epub/file/to/parse'  # epub文件的存放路径

# summary的相关参数
summary_len = 50  # summary的token长度
header = '用不超过' + str(summary_len) + '字总结这段文字：'
header_len = num_tokens_from_string(header)  # 提问头长度
body_max_len = MAX_SECTION_LEN - header_len  # 提问体最大长度


def epub_process(epub_name):
    # 获取全书的内容列表
    content_list = epub_parser(epub_name)  # 内容列表中的每条记录，都是全文的一个片段
    # 存储全书的总结内容，包括每若干个片段，每章，直到全书
    total_summary_list = []
    # 递归总结每个章节的内容
    segment_summary(header, body_max_len, content_list, total_summary_list, True)
    # 递归总结全书的内容
    chapter_summary(header, body_max_len, content_list, total_summary_list)
    # 将总结内容保存到硬盘中
    write_summary_to_csv(summary_file_name, total_summary_list)


if __name__ == '__main__':
    epub_process(book_name)
