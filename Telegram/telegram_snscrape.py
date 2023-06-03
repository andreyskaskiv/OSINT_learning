import json
import os
from datetime import datetime

import snscrape.modules.telegram as tg
from tqdm import tqdm


def scrape_posts(channel_name, max_results, target_date, filter_content):
    """Scrape posts"""
    empty_value = ""
    channel_data = {
        channel_name: {}
    }

    pbar = tqdm(total=max_results)
    for post in tg.TelegramChannelScraper(channel_name).get_items():
        if post.date.date() >= target_date.date():
            post_number = post.url.split("/")[-1]  # Extract post number from the URL
            post_data = {
                "url": post.url,
                "date": str(post.date),
                "content": post.content,
                "outlinks": post.outlinks,
                # "linkPreview": post.linkPreview,
            }
            if (filter_content in post_data['content']) or filter_content == empty_value:
                channel_data[channel_name][post_number] = post_data
                pbar.update(1)
                if len(channel_data[channel_name]) >= max_results:
                    break

    pbar.close()
    return channel_data


def save_to_json(channel_data, file_path):
    """Save to JSON"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(channel_data, f, ensure_ascii=False)


def run(channel_name, max_results, target_date, output_file, filter_content):
    """Run the scraping process"""
    channel_data = scrape_posts(channel_name, max_results, target_date, filter_content)
    save_to_json(channel_data, output_file)
    abs_output_file = os.path.abspath(output_file)
    print(f"Scraped data saved to {output_file}")
    print(f"View the file: file://{abs_output_file}")


if __name__ == "__main__":
    """
    :param channel_name: telegram-channel, for example: xor_journal
    :param max_results: only return the first N results
    :param target_date: only return results newer than target_date
    :param output_file: name output file
    :param filter_content: filter content
    :return: channel_name.json {"xor_journal": {
                                    "post number": {
                                      "url": "",
                                      "date": "",
                                      "content": "",
                                      "outlinks": []
                                    },
                                    ...}}
    """

    channel_name = "xor_journal"
    max_results = 10
    target_date = datetime(2023, 6, 1)
    output_file = f'{channel_name}.json'
    filter_content = ""  # Replace with the desired content of the filter or leave the value blank to not filter

    run(channel_name, max_results, target_date, output_file, filter_content)
