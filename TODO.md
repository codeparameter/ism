README
users -> User Model(with role) + Role Model + Factory Model + UserFactory Model
invoices -> Model(status, total price, date of order, date of ...(eachProcess)), new orders and previous orders can be filtered by status
blocks -> price for showing in invoice + status (available, sold(ordered, applied))
app name > module > method or var or ... > more depth ... : description
blocks > pop_pics_ids ViewSet method
blocks > add_vids_ids ViewSet method
blocks > pop_vids_ids ViewSet method
Pic > signals > post delete: pop_pics_ids 
Vid > signals > post delete: pop_vids_ids
blocks > pic_reorder ViewSet method: takes 2 args: pic_id (not index of it in pics list), idx to insert
blocks > vid-reorder ViewSet method: takes 2 args: pic_id (not index of it in pics list), idx to insert