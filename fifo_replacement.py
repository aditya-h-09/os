def fifo(page_reference_string, num_page_frames):
    page_faults = 0
    page_frames = []
    for page in page_reference_string:
        if page not in page_frames:
            if len(page_frames) < num_page_frames:
                page_frames.append(page)
            else:
                page_frames.pop(0)
                page_frames.append(page)
            page_faults += 1
        else:
            pass
        print(f"Page Reference String: {page}, Page Frames: {page_frames}")
    print(f"Total Page Faults (FIFO): {page_faults}")



fifo_page_reference_string = [1, 3, 0, 3, 5, 6, 3]
fifo_num_page_frames = 3

print("FIFO Page Replacement:")
fifo(fifo_page_reference_string, fifo_num_page_frames)
