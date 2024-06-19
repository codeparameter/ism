README
app name > module > method or var or ... > more depth ... : description
blocks > pop_pics_ids ViewSet method
blocks > add_vids_ids ViewSet method
blocks > pop_vids_ids ViewSet method
Pic > signals > post delete: pop_pics_ids 
Vid > signals > post delete: pop_vids_ids
blocks > pic_reorder ViewSet method: takes 2 args: pic_id (not index of it in pics list), idx to insert
blocks > vid-reorder ViewSet method: takes 2 args: pic_id (not index of it in pics list), idx to insert