def get_consective_items(items, key): 
    items = str(items)
    key = str(key)
    max_cons_count = 0
    cons_count = 0

    for i in items:
        if i == key:
             cons_count += 1
        else:
            if cons_count > max_cons_count:
                max_cons_count = cons_count
            cons_count = 0

    if cons_count > max_cons_count:
        max_cons_count = cons_count
    
    return max_cons_count
