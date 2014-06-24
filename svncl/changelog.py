import datetime

import svn
import svn.local
import svn.remote

def generate(wd_path, tag_directory_url):
    s_tag = svn.remote.RemoteClient(tag_directory_url)
    tags = list(s_tag.log_default(limit=1))

    if not tags:
        raise ValueError("No tags found.")

    last_tag = tags[0]
    s_wd = svn.local.LocalClient(wd_path)
    search_start_dt = last_tag.date + datetime.timedelta(seconds=1)
    for e in s_wd.log_default(timestamp_from_dt=search_start_dt):
        yield e.msg.rstrip()
