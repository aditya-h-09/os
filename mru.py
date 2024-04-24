def mru_page_replacement(page_reference_string, num_frames):
    page_frames = [-1] * num_frames
    page_faults = 0

    for page in page_reference_string:
        if page not in page_frames:


            mru_index = max(range(len(page_frames)), key=lambda i: page_frames[::-1].index(page_frames[i]) if page_frames[i] in page_frames else -1)
            page_frames[mru_index] = page
            page_faults += 1
        else:

            page_frames.remove(page)
            page_frames.append(page)

    return page_faults

def main():
    page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
    num_frames = 4

    total_page_faults = mru_page_replacement(page_reference_string, num_frames)

    print("Total Page Faults using MRU Page Replacement Algorithm:", total_page_faults)

if __name__ == "__main__":
    main()
