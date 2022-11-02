from django.core.management.base import BaseCommand
import sqlite3
import pandas as pd
from django.utils import timezone

PATH = "static/data/"

CSV_TABLE = {
    "category.csv": "reviews_category",
    "genre.csv": "reviews_genre",
    "titles.csv": "reviews_title",
    "genre_title.csv": "reviews_title_genre"
}


class Command(BaseCommand):
    help = 'import data csv file to table on DB'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write(f"Импорт данных запущен: {time}")
        conn = sqlite3.connect('db.sqlite3')
        for file_name, table_name in CSV_TABLE.items():
            df = pd.read_csv(f"{PATH}/{file_name}")
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            self.stdout.write(f"Импорт в {table_name} завершен: {time}")
