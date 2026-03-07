import re
import json
import os


def parse_receipt(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    content = None
    for encoding in ['utf-8', 'windows-1251', 'cp1251']:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            if content and len(content) > 0:
                break
        except:
            continue
    
    if not content:
        print("ERROR: Could not read file!")
        return
    
    result = {}
    
    dt_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', content)
    result['date_time'] = dt_match.group(1) if dt_match else "N/A"
    
    payment_match = re.search(r'Банковская карта:\s*\n\s*([\d\s]+,\d{2})', content)
    
    if payment_match:
        result['payment_method'] = 'Банковская карта'
        result['payment_amount'] = payment_match.group(1).replace(' ', '')
    else:
        result['payment_method'] = 'Unknown'
        result['payment_amount'] = 'N/A'
    
    total_match = re.search(r'ИТОГО:\s*\n\s*([\d\s]+,\d{2})', content)
    
    if total_match:
        result['receipt_total'] = total_match.group(1).replace(' ', '')
    else:
        result['receipt_total'] = "N/A"
    
    items = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if re.match(r'^\d+\.$', line):
            
            product_name = ""
            quantity = ""
            unit_price = ""
            item_total = ""
            
            i += 1
            
            while i < len(lines):
                name_line = lines[i].strip()
                
                if ' x ' in name_line and ',' in name_line:
                    parts = name_line.split(' x ')
                    if len(parts) == 2:
                        quantity = parts[0].strip().replace(' ', '')
                        unit_price = parts[1].strip().replace(' ', '')
                    i += 1
                    break
                
                if name_line == '' or name_line == 'Стоимость':
                    i += 1
                    continue
                
                if re.match(r'^\d+\.$', name_line):
                    i -= 1
                    break
                
                product_name += name_line + " "
                i += 1
            
            product_name = product_name.strip()
            
            if i < len(lines):
                total_line = lines[i].strip()
                if re.match(r'^[\d\s]+,\d{2}$', total_line):
                    item_total = total_line.replace(' ', '')
                    i += 1
            
            if product_name and quantity and unit_price:
                items.append({
                    'name': product_name,
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'total': item_total
                })
        else:
            i += 1
    
    result['items'] = items
    result['items_count'] = len(items)
    
    calculated = 0.0
    
    for item in items:
        try:
            qty = float(item['quantity'].replace(',', '.'))
            price = float(item['unit_price'].replace(',', '.'))
            calculated += qty * price
        except ValueError:
            pass
    
    result['calculated_total'] = f"{calculated:,.2f}".replace(',', 'X').replace('.', ',').replace('X', ' ')
    
    json_path = os.path.join(script_dir, 'parsed_receipt.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"Date/Time: {result['date_time']}")
    print(f"Payment: {result['payment_method']} - {result['payment_amount']} KZT")
    print(f"Total: {result['receipt_total']} KZT")
    print(f"Items: {result['items_count']}")
    print(f"Saved to: {json_path}")
    
    return result


if __name__ == "__main__":
    parse_receipt('raw.txt')