def lru_page_replacement(page_reference_string, num_frames):
    page_frames = []
    page_faults = 0
    
    for page in page_reference_string:
        if page not in page_frames:
            if len(page_frames) < num_frames:
                page_frames.append(page)
            else:

                lru_page = min(page_frames, key=page_reference_string[::-1].index)
                page_frames[page_frames.index(lru_page)] = page
            page_faults += 1
        else:

            page_frames.remove(page)
            page_frames.append(page)
    
    return page_faults


page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
num_frames = 4
total_page_faults = lru_page_replacement(page_reference_string, num_frames)
print("Total number of page faults using LRU:", total_page_faults)
