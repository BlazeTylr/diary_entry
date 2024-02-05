from lib.diary_entry import *

def test_diary_entry_init():
    entry = DiaryEntry('The universe', 'Written by Stephen Hawking')
    actual = {'title': entry.title, 'contents': entry.contents}
    expected = {'title': 'The universe', 'contents': 'Written by Stephen Hawking'}
    assert actual == expected

def test_diary_entry_format():
    entry = DiaryEntry('The Universe', 'Written by Stephen Hawking')
    actual = entry.format()
    expected = 'The Universe: Written by Stephen Hawking'
    assert actual == expected

def test_diary_entry_count_words():
    entry = DiaryEntry('The Universe', 'Written by Stephen Hawking')
    actual = entry.count_words()
    expected = 4
    assert actual == expected

def test_diary_entry_reading_time():
    entry = DiaryEntry('The Universe', 'Written by Stephen Hawking')
    actual = entry.reading_time(4)
    expected = 1
    assert actual == expected

def test_diary_entry_reading_chun_return_chunk():
    entry = DiaryEntry('The Universe', 'Written by Stephen Hawking')
    actual = entry.reading_chunk(2,1)
    expected = 'Written by'
    assert actual == expected

def test_diary_entry_reading_chun_return_2_chunks():
    entry = DiaryEntry('The Universe', 'Written by Stephen Hawking')
    entry.reading_chunk(2,1)
    actual = entry.reading_chunk(2,1)
    expected = 'Stephen Hawking'
    assert actual == expected

def test_diary_entry_reading_chun_return_several_chunks():
    entry = DiaryEntry('The Universe', 'Written by Stephen Hawking')
    entry.reading_chunk(2,1)
    entry.reading_chunk(2,1)
    actual = entry.reading_chunk(2,1)
    expected = 'Written by'
    assert actual == expected


