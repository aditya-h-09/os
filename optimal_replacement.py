def optimal(page_reference_string, num_page_frames):
    page_faults = 0
    page_frames = []
    for i, page in enumerate(page_reference_string):
        if page not in page_frames:
            if len(page_frames) < num_page_frames:
                page_frames.append(page)
            else:
                index_to_replace = -1
                farthest_used = -1
                for frame_index, frame in enumerate(page_frames):
                    if frame not in page_reference_string[i+1:]:
                        index_to_replace = frame_index
                        break
                    elif page_reference_string[i+1:].index(frame) > farthest_used:
                        farthest_used = page_reference_string[i+1:].index(frame)
                        index_to_replace = frame_index
                page_frames[index_to_replace] = page
            page_faults += 1
        else:
            pass
        print(f"Page Reference String: {page}, Page Frames: {page_frames}")
    print(f"Total Page Faults (Optimal): {page_faults}")


# Page reference string and page frames for Optimal
optimal_page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
optimal_num_page_frames = 4

print("Optimal Page Replacement:")
optimal(optimal_page_reference_string, optimal_num_page_frames)
