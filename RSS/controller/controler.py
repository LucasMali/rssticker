
from RSS.model.rssfeed import RssModel
# from RSS.view.rssticker import RssView ##This RssView is still unwritten as of now
import csv


class RssController:
    list_urls = [""]
    list_iterator = None
    rss_model = None
    rss_view = None

    def __init__(self):
        self.list_iterator = iter(list)
        self.rss_model = RssModel
        # self.rss_view = RssView

    def load_urls(self):
        with open('list_urls.csv', newline='') as f:
            reader = csv.reader(f) # this CSV is in the controller folder
            list_urls = list(reader)
            self.list_urls = list(reader)
            # list_urls = list(reader)
            # return list_urls

    def next_url(self):
        return next(self.list_iterator)

    def main(self):
        self.load_urls()

        try:
            _url = self.next_url()
        except StopIteration:
            pass
        try:
            if self.rss_model._newsreel_index_pos == 0:
                _rss_model = self.rss_model.parse(_url)
                _newsreel = self._rss_model.get_current()
                # pass newsreel into the view here
                # sleep x number of seconds?
                _newsreel = self._rssmodel.get_next()

        except Exception as e:
            pass

        def next_url_fail(self):
            pass

    def load_file_fail(self):
        pass


if __name__ == "__main__":
    RssController().main()

    # list_urls = load_urls(self=list_urls)
    # next_url = next_url(list_urls)
    # print(list_urls)
    # print(next_url)